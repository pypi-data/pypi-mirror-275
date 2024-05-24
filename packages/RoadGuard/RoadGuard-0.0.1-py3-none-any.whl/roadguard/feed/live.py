import cv2
import pyaudio
import wave
import speech_recognition as sr
import numpy as np
import threading


# Initialize class (for recognizing the speech)
def clip():
    r = sr.Recognizer()
    return r


def capture_audio(segment_length=5, filename_prefix="output"):
    # Setup the audio recording parameters
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1  # Mono audio
    RATE = 44100  # Sample rate
    CHUNK = 1024  # Buffer size
    RECORD_SECONDS = segment_length  # Length of each audio file segment

    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    try:
        while True:
            frames = []

            # Record data for a set number of seconds
            for _ in range(int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            # Generate filename based on the current timestamp
            filename = f"{filename_prefix}_{int(time.time())}.wav"

            # Save the recorded data as a WAV file
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))

            print(f"Saved: {filename}")

    except KeyboardInterrupt:
        print("Recording stopped")

    finally:
        # Stop and close the stream and terminate the PyAudio object
        stream.stop_stream()
        stream.close()
        audio.terminate()


# Function to apply mosaic to a region of interest (ROI)
def apply_mosaic(frame, x, y, w, h, factor=10):
    roi = frame[y:y + h, x:x + w]
    roi = cv2.resize(roi, (w // factor, h // factor), interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y:y + h, x:x + w] = roi
    return frame


# Function to process video frames
def process_video(command):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_licence_plate_rus_16stages.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces and plates
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        plates = plate_cascade.detectMultiScale(frame, 1.3, 5)

        # Apply mosaic to faces and plates
        for (x, y, w, h) in faces:
            frame = apply_mosaic(frame, x, y, w, h)
        for (x, y, w, h) in plates:
            frame = apply_mosaic(frame, x, y, w, h)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main function to run the demo
def main():
    # Start a thread for audio capture
    while True:
        command = capture_audio()
        if command and 'start' in command.lower():
            process_video(command)


# Run the main function
if __name__ == "__main__":
    main()
