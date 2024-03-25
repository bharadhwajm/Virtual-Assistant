import check_input
import random
import speak

def flip_coin():
    coin_toss = random.randint(1, 2)
    if coin_toss == 1:
        speak.speak("its tails")
        return check_input.check_input()
    else:
        speak.speak("its heads")
        return check_input.check_input()

def random_number(user_input):
    num = []
    count = 0
    for i in user_input:
        if i.isdigit():
            num.append(int(i))
            count += 1
            if count == 2:
                num.sort()
                choosen_number = random.randint(num[0], num[1])
                print(choosen_number)
                speak.speak("the number is {}".format(str(choosen_number)))
                return check_input.check_input()
    else:
        choosen_number = random.randint(0, 100)
        print(choosen_number)
        speak.speak("the number is {}".format(str(choosen_number)))
        return check_input.check_input()

def roll_dice():
    dice_num = random.randint(1, 6)
    speak.speak("{}".format(str(dice_num)))
    return check_input.check_input()
