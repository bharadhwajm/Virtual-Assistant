import check_input
import speak
import wolframalpha
from PyDictionary import PyDictionary


def dictionary(user_asked):
    #! searches for meanings of words from PyDictionary module
    to_strip = ['what', 'what\'s', 'mean',
                'meaning', 'of', 'is', 'does', 'the', 'tell']
    for i in user_asked:
        if i not in to_strip:
            meaning = PyDictionary.meaning(i)
            if meaning == 'NONE':
                return speak.speak("i couldn't understand you... Please try again")
            else:
                speak.speak("{}".format(meaning))
                return check_input.check_input()


def search(to_search):
    butcher_client = wolframalpha.Client('XXXXXXXXXXX') #API key for wolframAlpha
    butcher_ask = butcher_client.query(to_search)
    try:
        answer = next(butcher_ask.results).text
        print("wolframalpha")
        print(answer)
        return speak.speak(answer)
    except StopIteration:
        speak.speak("I'm not able to find an answer for your question")
        return check_input.check_input()