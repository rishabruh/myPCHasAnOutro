import os
from pydub import AudioSegment
from pydub.playback import play
import threading
from time import sleep

def theThing():
    sleep(0.5)
    for i in range(0,10):
        print(f'Shutting down in {10-i} seconds')
        sleep(1)
    print("goodbye :)")
    exit()

def song_f():
    song=AudioSegment.from_mp3('outro.mp3')
    play(song)

def shutd():
    os.system("shutdown /s /t 1")

if __name__=="__main__":
    choice=input("This will shutdown your computer\nMake sure no apps are open\nProceed?(Ctrl+C to abort now/Enter to start) ")
    if choice.lower=='n':
        exit()
    song_t=threading.Thread(target=song_f)
    thing=threading.Thread(target=theThing)
    shutd_t=threading.Thread(target=shutd)
    thing.start()
    song_t.start()
    sleep(19)
    shutd_t.start()
