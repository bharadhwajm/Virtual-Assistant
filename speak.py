from gtts import gTTS
import os

def speak(to_speak):
    try:
        #! speaks answers through gtts module
        voice = gTTS(text=to_speak, lang='en', tld='fr')
        voice.save('speak.mp3')
        os.system('mpg123 speak.mp3')

    except AssertionError:
        #! if couldn't speak something returns following reply
        return speak("i couldn't find an answer for the question")