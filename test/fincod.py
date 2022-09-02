# Stop the Sound via multiprocessing
import multiprocessing
from playsound import playsound

pelle = playsound("file.mp3")


p = multiprocessing.Process(target=pelle)
p.start()
input("press ENTER to stop playback")
p.terminate()
