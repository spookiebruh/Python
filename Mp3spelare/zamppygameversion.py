from os import remove
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

#Function to add multiple songs to the player
 
def add_multiple_songs():
    songs = filedialog.askopenfilenames(initialdir='C:/Users/zackarias.edlundsve/Music', title="Choose songs", filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav"), ))

    for song in songs:
        song = song.replace("C:/Users/zackarias.edlundsve/Music/", "")
        song = song.replace(".mp3", "")
        song = song.replace(".wav", "")

        song_list.insert(END, song)



#Function that removes selected song
def remove_song():
    song = song_list.curselection()
    song_list.delete(song)

#Function that removes all songs 
def remove_all():
    song_list.delete(0, END)

    mixer.music.stop()

playstate = False
pausestate = False


#Play song
def play():
    song = song_list.get(ACTIVE)
    song = f'C:/Users/zackarias.edlundsve/Music/{song}.mp3'
    mixer.music.load(song)
    mixer.music.play(loops=0)

    get_song_time()
        


#Stop current song
def stop():
    mixer.music.stop()
    song_list.selection_clear(ACTIVE)

#Pause current song
def pause():
    global pausestate
    if pausestate == False:
        pausestate = True
        mixer.music.pause()
    else:
        pausestate = False
        mixer.music.unpause()
        
        

def playNext():
    nextSong = song_list.curselection()
    nextSong = nextSong[0] + 1
    nextSongName = song_list.get(nextSong)
    nextSongName = f'C:/Users/zackarias.edlundsve/Music/{nextSongName}.mp3'

    mixer.music.load(nextSongName)
    mixer.music.play()

    song_list.select_clear(0, 'end')
    song_list.activate(nextSong)
    song_list.select_set(nextSong)

def playPrev():
    prevSong = song_list.curselection()
    prevSong = prevSong[0] - 1
    prevSongName = song_list.get(prevSong)
    prevSongName = f'C:/Users/zackarias.edlundsve/Music/{prevSongName}.mp3'

    mixer.music.load(prevSongName)
    mixer.music.play()

    song_list.select_clear(0, 'end')
    song_list.activate(prevSong)
    song_list.select_set(prevSong)


#Show time of song
def get_song_time():


    song_time = mixer.music.get_pos() /1000
    song_time_converted = time.strftime("%H:%M:%S", time.gmtime(song_time))
    information_bar.config(text=song_time_converted)
    
    information_bar.after(1000, get_song_time)
    


#Song list
song_list = Listbox(window, bg="black", fg="cyan", width=50, selectbackground="gray", selectforeground="black")
song_list.pack(pady=20)


#Buttons control frame
controls_frame = Frame(window)
controls_frame.pack()

#Bar to show playtime and other information
information_bar = Label(window, text="", bd=1, relief=GROOVE, anchor=E)
information_bar.pack(fill=X, side=BOTTOM, ipady=2)

#Create buttons for player
prev_button = Button(controls_frame,text="Prev", command = playPrev)
next_button = Button(controls_frame, text="Next", command=playNext)
play_button = Button(controls_frame,text="Play", command=play)
pause_button = Button(controls_frame,text="Pause", command=pause)
stop_button = Button(controls_frame,text="Stop", command=stop)

prev_button.grid(row=0, column=0)
next_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(4,weight=1)

window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(1,weight=1)
window.grid_rowconfigure(2,weight=1)
window.grid_rowconfigure(3,weight=1)
window.grid_rowconfigure(4,weight=1)


#Create menu
top_menu = Menu(window)
window.config(menu=top_menu)

#Menu to add songs
menu_addSong = Menu(top_menu)
top_menu.add_cascade(label="Add song", menu=menu_addSong)
menu_addSong.add_command(label="Add one song to playlist", command=add_song)
menu_addSong.add_command(label="Add multiple songs to playlist", command=add_multiple_songs)


#Menu to remove song
menu_removeSong = Menu(top_menu)
top_menu.add_cascade(label="Remove song", menu=menu_removeSong)
menu_removeSong.add_command(label="Remove song from list", command=remove_song)
menu_removeSong.add_command(label="Remove all songs", command=remove_all)

window.mainloop()







