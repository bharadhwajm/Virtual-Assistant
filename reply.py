import json
import speak
import random
import check_input

def butcher_says(replies_to):
    #! speaks some pre given answers from butcher_tasks.json file
    with open('/home/bharadhwaj/personal-code/python/BUTCHER/replies.json') as can_say:
        replies = json.load(can_say)
        for i in replies["things butcher can say"]:
            if i in replies_to:
                print(i)
                for j in replies["things butcher can say"][i]:
                    if j in replies_to:
                        if type(replies["things butcher can say"][i][j]) == list:
                            speak.speak(random.choice(replies["things butcher can say"][i][j]))
                            return check_input.check_input()
                        else:
                            speak.speak(replies["things butcher can say"][i][j])
                            return check_input.check_input()


def user_info(ask_info):
    #! speaks user's given information from json file
    with open('/home/bharadhwaj/personal-code/python/BUTCHER/replies.json') as user_info:
        info = json.load(user_info)
        for i in info["things butcher say about you"]:
            if i in ask_info:
                for j in info["things butcher say about you"][i]:
                    if j in ask_info:
                        if type(info["things butcher say about you"][i][j]) == dict:
                            for k in info["things butcher say about you"][i][j]:
                                if k in ask_info:
                                    if "birthday" in ask_info:
                                        speak.speak("your birthday is on {}".format(info["things butcher say about you"][i][j][k]))
                                        return check_input.check_input()
                                    elif "born" in ask_info:
                                        speak.speak("your born on {}".format(info["things butcher say about you"][i][j][k]))
                                        return check_input.check_input()
                                    else:
                                        word_list = ['name', 'age', 'old','i']
                                        for word in word_list:
                                            if word in ask_info:
                                                speak.speak("your {}".format(info["things butcher say about you"][i][j][k]))
                                                return check_input.check_input()
                                        else:
                                            speak.speak("{}".format(info["things butcher say about you"][i][j][k]))
                                            return check_input.check_input()

                        else:
                            if 'birthday' in ask_info:
                                speak.speak("you birthday is on {}".format(info["things butcher say about you"][i][j]))
                                return check_input.check_input()
                            elif 'born' in ask_info:
                                speak.speak("your born on {}".format(info["things butcher say about you"][i][j]))
                                return check_input.check_input()
                            else:
                                word_list=['name','age','old','i']
                                print(ask_info)
                                for word in word_list:
                                    if word in ask_info:
                                        speak.speak("your {}".format(info["things butcher say about you"][i][j]))
                                        return check_input.check_input()
                                else:
                                    speak.speak("{}".format(info["things butcher say about you"][i][j]))
                                    return check_input.check_input()