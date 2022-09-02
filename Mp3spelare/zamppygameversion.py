from tkinter import *
import tkinter as tk
from pygame import mixer

            
#Creates window
window = Tk()
window.title("Z-Amp")
window.geometry("350x550")

mixer.init()

song_list = Listbox(window, bg="black", fg="cyan", width=50).pack(pady=20)


window.mainloop()







