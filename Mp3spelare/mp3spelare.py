from playsound import playsound
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#Function to play song of your choice (will change to a button)
def play_song():
    playsound(songchoice)



#Function to choose song (will change to an entry box)
#def choose_song():#
   # global songchoice 
    #songchoice = input(str("Write path to song you would like to play (this player sucks so the file has to be 32kHz or lower bitrate to play) "))



#Creates window with dimensions i like
window = Tk()
window.title("ZAmp")
window.geometry('350x550')


canvas1 = tk.Canvas(window, width = 350, height = 550)
canvas1.pack()

songchoice = tk.Entry(window)
canvas1.create_window(200, 140, window=songchoice)

play_button = tk.Button(window, text="Play", width=50, height=50, command=playsound)


#Main while loop
while 1 > 0:
    #choose_song()
    play = input(str("What do you want to do? 1. Play 2. Exit "))
    if play == "1":
        play_song()
    if play == "2":
        break
        exit
    else:
        print("Choose 1 or 2 please.")
        play = input(str("What do you want to do? 1. Play 2. Exit")) 

window.mainloop()




#while 1 > 0:
           # playsound("C:/Users/zackarias.edlundsve/Music/Death Grips - Exmilitary - 2 - Guillotinelowbit.mp3")
           # stop = input(str("Stop? Input 1 "))
          #  if stop == "1":
          #      continue
          #  else:
          #      print("Choose 1 or nothing please.")
          #      stop = input(str("Stop? Input 1 "))