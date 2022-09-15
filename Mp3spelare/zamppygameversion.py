from os import remove
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from webbrowser import get
from pygame import mixer
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
            
#Creates window
window = Tk()
window.title("Z-Amp")
window.geometry("350x550")

mixer.init()

playlist = [] #New list to store paths instead of names to load songs from.
root_path = "C:/Users/zackarias.edlundsve/Music/"
#Function to add song
def add_song():
    global song

    song = filedialog.askopenfilename(title="Choose song", filetypes=((".mp3", "*.mp3"), (".wav", "*.wav"), ))

    song = song.replace(root_path, "")
    song_list.insert(END, song)


#Function to add multiple songs to the player
def add_multiple():
    global songs
    global song

    songs = filedialog.askopenfilenames(title="Choose songs", filetypes=((".mp3", "*.mp3"), (".wav", "*.wav"), ))
    for song in songs:
        song = song.replace(root_path, "")
        mixer.music.queue(f"C:/Users/zackarias.edlundsve/Music/{song}")
        song_list.insert(END, song)

#Function that removes selected song
def remove_song():
    song = song_list.curselection()
    song_list.delete(song)

#Function that removes all songs 
def remove_all():
    song_list.delete(0, END)

    mixer.music.stop()


pausestate = False

#Play song
def play():
    song = song_list.get(ACTIVE)
    song = f"C:/Users/zackarias.edlundsve/Music/{song}"
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
        get_song_time()
        
        
#Skip to next song in list
def playNext():
    nextSong = song_list.curselection()
    nextSong = nextSong[0] + 1
    nextSongName = song_list.get(nextSong)
    nextSongName = f'C:/Users/zackarias.edlundsve/Music/{nextSongName}'

    mixer.music.load(nextSongName)
    mixer.music.play()

    song_list.select_clear(0, 'end')
    song_list.activate(nextSong)
    song_list.select_set(nextSong)

    if not song_list:
        messagebox.showerror("No more songs")

#Skip to previous song in list
def playPrev():
    prevSong = song_list.curselection()
    prevSong = prevSong[0] - 1
    prevSongName = song_list.get(prevSong)
    prevSongName = f'C:/Users/zackarias.edlundsve/Music/{prevSongName}'

    mixer.music.load(prevSongName)
    mixer.music.play()

    song_list.select_clear(0, 'end')
    song_list.activate(prevSong)
    song_list.select_set(prevSong)


#Show time of song
def get_song_time():

    song_time = mixer.music.get_pos() /1000

    progress_label.config(text=f"Slider: {int(song_progress_bar.get())} and Song Pos: {int(song_time)}")

    song_time_converted = time.strftime("%H:%M:%S", time.gmtime(song_time))



    #Grab song from the list, load it using mutagen lib.
    cur_song = song_list.curselection()
    song = song_list.get(cur_song)
    song = f'C:/Users/zackarias.edlundsve/Music/{song}'
    song_mutagen = MP3(song)

    #Loads song info through mutagen
    global song_length
    song_length = song_mutagen.info.length
    converted_song_length = time.strftime("%H:%M:%S", time.gmtime(song_length))

    
    if int(song_progress_bar.get()) == song_time:
        #bar hasn't been moved
        song_time =+ 1

        bar_position = int(song_length)
        song_progress_bar.config(to=bar_position, value=int(song_time))
    else:
        song_time =+ 1

        bar_position = int(song_length)
        song_progress_bar.config(to=bar_position, value=int(song_progress_bar.get()))

        song_time_converted = time.strftime("%H:%M:%S", time.gmtime(int(song_progress_bar.get())))

        information_bar.config(text=f"{song_time_converted}/{converted_song_length}")

        song_continue = int(song_progress_bar.get()) + 1
        song_progress_bar.config(value=song_continue)
        


    #Converts song length to my time format of 

    #information_bar.config(text=f"{song_time_converted}/{converted_song_length}")
       
    #information_bar.config(text=song_length_converted)

    #song_progress_bar.config(value=int(song_time))

    #Update the bar to be on the postition of the song


    information_bar.after(1000, get_song_time)

def songBar(x):
    #progress_label.config(text=f'{int(song_progress_bar.get())}/{converted_song_length}')
     
    song = song_list.get(ACTIVE)
    song = f"C:/Users/zackarias.edlundsve/Music/{song}"
    mixer.music.load(song)
    mixer.music.play(loops=0, start=int(song_progress_bar.get()))


#vol = 0.5
#mixer.music.set_volume(vol)
#def volume_up():
#    global vol
#    vol =+ 0.1
    
    
#inactive_ticks = 0   

#if not mixer.get_busy():
#    inactive_ticks += 1

#    if inactive_ticks == 100:
#        # Play the next song
#        inactive_ticks = 0
#        playNext()


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
#volup_button = Button(controls_frame,text="+", command=volume_up)

#Put buttons in grid
prev_button.grid(row=0, column=0)
next_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)
#volup_button.grid(row=0, column=5)

#Configure grid to scale with window (doesn't work)
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
menu_addSong.add_command(label="Add multiple songs to playlist", command=add_multiple)


#Menu to remove song
menu_removeSong = Menu(top_menu)
top_menu.add_cascade(label="Remove song", menu=menu_removeSong)
menu_removeSong.add_command(label="Remove song from list", command=remove_song)
menu_removeSong.add_command(label="Remove all songs", command=remove_all)

#Song slider
song_progress_bar = ttk.Scale(window, from_=0, to=100, orient=HORIZONTAL, value=0, length=300, command=songBar)
song_progress_bar.pack(pady=20)

#Progressbar label
progress_label=Label(window, text="0")
progress_label.pack(pady=10)



window.mainloop()

