from tkinter import *
import tkinter as tk
from tkinter import filedialog
from webbrowser import get
from pygame import mixer
import time

            
#Creates window
window = Tk()
window.title("Z-Amp")
window.geometry("350x550")

mixer.init()

#Function to add song
def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Users/zackarias.edlundsve/Music', title="Choose song", filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav"), ))

    #Remove file path info and .mp3/.wav
    song = song.replace("C:/Users/zackarias.edlundsve/Music/", "")
    song = song.replace(".mp3", "")
    song = song.replace(".wav", "")

    #Insert file into song list
    song_list.insert(END, song)

playstate = 0

#Play song
def play():
    song = song_list.get(ACTIVE)
    song = f'C:/Users/zackarias.edlundsve/Music/{song}.mp3'
    mixer.music.load(song)
    mixer.music.play(loops=0)
    playstate = 1

#Stop current song
def stop():
    mixer.music.stop()
    song_list.selection_clear(ACTIVE)

#Pause current song
def pause():
    global pausestate
    pausestate = 0
    if pausestate == 0:
        mixer.music.pause()
        pausestate = 1
    elif pausestate == 1:
        mixer.music.unpause()
        pausestate = 0

#Show time of song
def get_song_time():
    song_time = mixer.music.get_pos
    while True:
        print(song_time)
        time.sleep(1)


#Song list
song_list = Listbox(window, bg="black", fg="cyan", width=50, selectbackground="gray", selectforeground="black")
song_list.pack(pady=20)


#Buttons control frame
controls_frame = Frame(window)
controls_frame.pack()



#Create buttons for player
next_button = Button(controls_frame, text="Next")
prev_button = Button(controls_frame,text="Prev")
play_button = Button(controls_frame,text="Play", command=play)
pause_button = Button(controls_frame,text="Pause", command=pause)
stop_button = Button(controls_frame,text="Stop", command=stop)

next_button.grid(row=0, column=0)
prev_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

#Create menu
top_menu = Menu(window)
window.config(menu=top_menu)

#Song to add songs
menu_addSong = Menu(top_menu)
top_menu.add_cascade(label="Add song", menu=menu_addSong)
menu_addSong.add_command(label="Add one song to playlist", command=add_song)

window.mainloop()







