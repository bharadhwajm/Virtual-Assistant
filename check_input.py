import calendar_time
import open_app_websites
import search
import reply
import speak
import json
import play_songs
import luck
import random
import listen

def check_input():
    print("listening")
    try:
        user_input=listen.recognize()
        user_input_split = user_input.split()
        for i in user_input_split:
            if user_input_split.count(i)>1:
                user_input_split.remove(i)
    except AttributeError:
        return check_input()
    
    #! to get ans from butcher
    ask_butcher=['you','your','a','who','joke','name','funny','how','doing']
    count=0
    for i in user_input_split:
        if i in ask_butcher:
            count+=1
    if count>1:
        return reply.butcher_says(user_input_split)

    #! get ans from butcher about you
    butcher_about_you=['i','born','my','am',
                        'name','i\'m','sad','happy','age','birthday']
    count=0
    for i in user_input_split:
        if i in butcher_about_you:
            count+=1
    if count>1:
        return reply.user_info(user_input_split)

    #! roll a dice
    roll_dice = ["roll", "dice"]
    count = 0
    for i in user_input_split:
        if i in roll_dice:
            count += 1
    if count > 1:
        return luck.roll_dice()
    
    #! flip coin
    flip_coin=["flip", "coin", "heads", "tails"]
    count = 0
    for i in user_input_split:
        if i in flip_coin:
            count += 1
    if count > 1:
        if 'heads' and 'tails'in user_input_split:
            return luck.flip_coin()
        elif 'flip' and 'coin' in user_input_split:
            return luck.flip_coin()
    
    #! pick random number
    random_num= ["pick", "number", "random","from","to","between"]
    count = 0
    for i in user_input_split:
        if i in random_num:
            count += 1
    if count > 1:
        return luck.random_number(user_input_split)

    #! to get day date and time and create timer
    ask_calendar = ['the', 'day', 'date', 'time',
                    'today', 'today\'s', 'timer', 'keep', 'set', 'for','it']
    count = 0
    for i in user_input_split:
        if i in ask_calendar:
            count += 1
    if count > 1:
        if 'timer' in user_input_split:
            return calendar_time.timer(user_input_split)
        else:
            return calendar_time.calendar_time(user_input_split)

    #! to search dictionary
    ask_dict = ['meaning', 'mean']
    for i in user_input_split:
        if i in ask_dict:
            return search.dictionary(user_input_split)

    #! to search wolfram alpha
    ask_search = ['what', 'what\'s', 'who', 'is', 'are', 'was', 'of', 'the', 'made',
                  "when", "how", 'synonym', 'opposite', 'antonym','president','minister','ceo']
    count = 0
    for i in user_input_split:
        if i in ask_search:
            count += 1
    if count > 0:
        return search.search(user_input)


    #! to play songs
    if "play" in user_input_split:
        if "songs" in user_input_split:
            return play_songs.play_songs_random()
        elif "song" in user_input_split:
            return play_songs.play_songs_random()
        else:
            return play_songs.play_specific_song(user_input)    

    #! open apps
    if "open" in user_input_split:
        with open('/home/bharadhwaj/personal-code/python/BUTCHER/tasks.json') as apps:
            to_open = json.load(apps)
            for i in to_open["open apps"]:
                if i in user_input_split:
                    return open_app_websites.open_app(i)

    #! to open websites
            for i in to_open["open websites"]:
                if i in user_input_split:
                    return open_app_websites.open_websites(i)
            else:
                speak.speak("i couldn't open {} try entering the website you want to add in the pop up".format(
                    user_input_split[-1]))
                return open_app_websites.add_websites()
        
    #! wishes
    wishes=['evening','morning','afternoon','night']
    for i in user_input_split:
        if i in wishes:
            return calendar_time.wishes(user_input_split)

    #! greet user
    greet_words = ["hello", 'hi']
    with open('/home/bharadhwaj/personal-code/python/BUTCHER/replies.json') as task:
        name=json.load(task)
        for i in greet_words:
            if i in user_input_split:
                return speak.speak(random.choice(["hello there"+name["things butcher say about you"]["my"]["name"], 'hi'+name["things butcher say about you"]["my"]["name"]]))
        
        else:
            for i in user_input_split:
                if i.isdigit():
                    return search.search(user_input)
            else:
                speak.speak("i couldn't understand you... please try again")
                return check_input()
