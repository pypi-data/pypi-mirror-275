import speech_recognition as sr


def trigger_and_run(func: callable,
                    catch_phrase: str = "catch"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"Listening for {catch_phrase} command...")
        try:
            while True:
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_sphinx(audio)
                    print(f"Recognized: {text}")
                    
                    if catch_phrase in text.lower():
                        func()

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from recognizer; {e}")
        except KeyboardInterrupt:
            print("Stopped listening")
