import os
import random
import speak

def play_songs_random():
    for i in os.listdir("/home/bharadh/songs"):
        song = random.choice(os.listdir("/home/bharadh/songs"))
        if " " in song:
            song_to_play = song.replace(" ", "\ ")
            os.system("mpg123 /home/bharadh/songs/"+song_to_play)
        else:
            os.system("mpg123 /home/bharadh/songs/"+song)

def play_specific_song(song):
    for i in os.listdir("/home/bharadh/songs"):
        if i.lower().replace(".mp3","") in song:
            if " " in i:
                song_to_play=i.replace(" ","\ ")
                os.system("mpg123 /home/bharadh/songs/"+song_to_play)
            else:
                os.system("mpg123 /home/bharadh/songs/"+i)
    else:
        return speak.speak("I couldn't find the song in the directory")
