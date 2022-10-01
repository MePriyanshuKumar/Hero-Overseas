
from tkinter import Tk, Button
from pygame import mixer

root = Tk()
root.title("Play Pause btn")
root.geometry('350x200')

mixer.init()
mixer.music.load("Cambridge IELTS 1 - Listening Test 1.mp3")

def play_music():
    if button["text"] == "Play":
        button["text"] = "Pause"
        button["bg"] = "red"
        mixer.music.play()
    else:
        button["text"] = "Play"
        button["bg"] = "orange"
        mixer.music.pause()

button = Button(root, text='Play', width=14, bg='orange', fg='black', command=play_music)
button.pack()

root.mainloop()


