import datetime
import speak
import time
import os
import speech_recognition
import sys

def calendar_time(user_input):
    #! gets current time
    if 'time' in user_input:
        time_now = datetime.datetime.now().strftime("%H:%M")
        return speak.speak("the time is {}".format(time_now))

    #! gets current day's date
    elif 'date' in user_input:
        date = datetime.date.today()
        print(date)
        return speak.speak("Today's date is {}".format(date))

    #! gets the day
    elif 'day' in user_input:
        day = datetime.datetime.today().strftime('%A')
        return speak.speak("Today is {}".format(day))

def timer(user_input): 
    #! a timer
    minutes = 0
    seconds = 0
    hours = 0
    for i in range(len(user_input)):
        if user_input[i] == "hour":
            if user_input[i-1].isdigit():
                hours += int(user_input[i-1])*3600
        elif user_input[i] == "hours":
            if user_input[i-1].isdigit():
                hours += int(user_input[i-1])*3600

        if user_input[i] == "minute":
            if user_input[i-1].isdigit():
                minutes += int(user_input[i-1])*60
        elif user_input[i] == "minutes":
            if user_input[i-1].isdigit():
                minutes += int(user_input[i-1])*60

        if user_input[i] == "second":
            if user_input[i-1].isdigit():
                seconds += int(user_input[i-1])
        elif user_input[i] == "seconds":
            if user_input[i-1].isdigit():
                seconds += int(user_input[i-1])

    timer_limit = hours+minutes+seconds
    if timer_limit==0:
        ask_time_limit=recognize()
        print(str(ask_time_limit))
        ask_time_limit_split=str(ask_time_limit).split()
        for i in ask_time_limit:
            if i.isdigit():
                print(i)
                return timer(ask_time_limit_split)
            else:
                return recognize()
    else:            
        speak.speak("your timer is starting")
        for i in range(timer_limit):
            time.sleep(1)
        os.system('mpg123 tone.mp3')

def recognize():
    #! listens to user
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as ears:
        speak.speak("how long do you want your timer for")

        try:
            #! recognizes the users voice command and converts into text
            recognizer.adjust_for_ambient_noise(ears)
            listen = recognizer.listen(ears)
            converted_text = recognizer.recognize_google(listen).lower()
            return converted_text

        except speech_recognition.UnknownValueError:
            #! if couldn't understand user's command
            sys.exit()

def wishes(user_input):
    time=int(datetime.datetime.now().strftime("%H"))
    actual_time=datetime.datetime.now().strftime("%H:%M")
    if 'morning' in user_input:
        if time<12:
            return speak.speak("good morning")
        else:
            return speak.speak("hey... it's not the morning... the time is{}".format(str(actual_time)))
    if 'afternoon' in user_input:
        if time>=12 and time<17:
            return speak.speak("Good afternoon")
        elif time<12:
            return speak.speak("hey... it's {} A.M right now".format(str(actual_time)))
        else:
            return speak.speak("hey its {} P.M right now".format(str(actual_time)))
    if 'evening' in user_input:
        if time>=17:
            return speak.speak("good evening")
        elif time<17 and time>=12:
            return speak.speak("hey... the time is {} P.M right now".format(str(actual_time)))
        else:
            return speak.speak("hey... the time is {} A.M right now".format(str(actual_time)))
    if 'night' in user_input:
        return speak.speak("good night")
