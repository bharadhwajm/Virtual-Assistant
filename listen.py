import speech_recognition

def recognize():
    #! listens to user
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as ears:

        try:
            #! recognizes the users voice command and converts into text
            recognizer.adjust_for_ambient_noise(ears)
            listen = recognizer.listen(ears)
            converted_text = recognizer.recognize_google(listen).lower()
            print(converted_text)
            return converted_text

        except speech_recognition.UnknownValueError:
            #! if couldn't understand user's command
            return