from playsound import playsound
from pygame import mixer
from tkinter import *
import tkinter as tk
import multiprocessing as mp
import time



#mp.freeze_support()
mixer.init()
mixer.music.load("file.mp3")
mixer.music.set_volume(0.3)
mixer.music.play()
chosensong = "C:/Users/zackarias.edlundsve/Music/Death Grips - Exmilitary - 2 - Guillotinelowbit.mp3"
#pelle = playsound(chosensong)
#Function to play song of your choice (will change to a button)
def play_song():
    playsound(chosensong)

#def song_process():

#if __name__ == "__main__":
mp.freeze_support()
songProcess = mp.Process(target=playsound, args=chosensong)
start_songProcess = songProcess.start()

#def stop_thread():
    #stopThread = threading.Thread(target=stop_song)
    #stopThread.start()

#Function to choose song (will change to an entry box)
#def choose_song():
 #   global songchoice 
  #  songchoice = input(str("Write path to song you would like to play (this player sucks so the file has to be 32kHz or lower bitrate to play) "))

#Creates window
window = Tk()
window.title("ZAmp")
window.geometry('350x550')

play_button = Button(window, text="Play", command=start_songProcess)
play_button.pack()

#stop_button = Button(window,text="Stop", command=stop_process)

canvas1 = tk.Canvas(window, width = 350, height = 550)
canvas1.pack()

songchoice = tk.Entry(window)
canvas1.create_window(200, 140, window=songchoice)


#Main while loop
#while 1 > 0:
    #choose_song()
    #play = input(str("What do you want to do? 1. Play 2. Exit "))
    #if play == "1":
       # play_song()
   # if play == "2":
   #     break
  #      exit
   # else:
   #     print("Choose 1 or 2 please.")
  #      play = input(str("What do you want to do? 1. Play 2. Exit")) 

window.mainaloop()




#while 1 > 0:
           # playsound("C:/Users/zackarias.edlundsve/Music/Death Grips - Exmilitary - 2 - Guillotinelowbit.mp3")
           # stop = input(str("Stop? Input 1 "))
          #  if stop == "1":
          #      continue
          #  else:
          #      print("Choose 1 or nothing please.")
          #      stop = input(str("Stop? Input 1 "))