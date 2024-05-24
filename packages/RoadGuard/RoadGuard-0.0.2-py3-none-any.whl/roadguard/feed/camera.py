import cv2
import time
import base64

from roadguard.feed import parameter


def add_mosaic(frame, x, y, w, h, factor=parameter.mosaic_factor):
    """Apply a mosaic to a region of the frame."""
    roi = frame[y:y + h, x:x + w]
    roi = cv2.resize(roi, (w // factor, h // factor),
                     interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h),
                     interpolation=cv2.INTER_NEAREST)
    frame[y:y + h, x:x + w] = roi
    return frame


def frame_to_base64(frame):
    """Convert a frame to a base64 string."""
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer).decode('utf-8')


def capture(
        duration=parameter.capture_duration,
        target_fps=parameter.target_fps):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
    )
    plate_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_license_plate_rus_16stages.xml'
    )

    # Calculate the interval between frames for the target frame rate
    frame_interval = 1 / target_fps
    last_capture_time = time.time()

    start_time = time.time()
    base64_frames = []

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()
        if current_time - last_capture_time >= frame_interval:
            last_capture_time = current_time

            # Detect faces and plates
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            plates = plate_cascade.detectMultiScale(frame, 1.3, 5)

            # Apply mosaic to faces and plates
            for (x, y, w, h) in faces:
                frame = add_mosaic(frame, x, y, w, h)
            for (x, y, w, h) in plates:
                frame = add_mosaic(frame, x, y, w, h)

            # Encode the frame to base64
            base64_frame = frame_to_base64(frame)
            base64_frames.append(base64_frame)

            # Display the resulting frame
            cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return base64_frames


def test():
    base64_encoded_frames = capture(5)
    print(len(base64_encoded_frames))


if __name__ == "__main__":
    test()
