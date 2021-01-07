from tkinter import *
from tkinter import filedialog
from pygame import mixer

#don't really like object oriented programming
class Mp3player:
    def __init__(self, pagewindow):
        pagewindow.geometry('800x400');pagewindow.title('Lola player');pagewindow.resizable(0,0)
        load = Button(pagewindow, text = 'Load ', width = 10, font = ('comic sans ms', 11), command = self.load)
        play = Button(pagewindow, text = 'Play', width = 10, font=('Times', 11), command = self.play)
        pause = Button(pagewindow, text = 'Pause', width = 10, font = ('Times', 11), command = self.pause)
        stop = Button(pagewindow, text = 'Stop', width = 12, font=('Times', 11), command = self.stop)
        load.place(x=0, y=20); play.place(x=110,y=20); pause.place(x=220, y=20); stop.place(x=330, y=20)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if  self.music_file:
            mixer.music.pause()
            self.playing_state = False
        else:
            mixer.music.unpause()
            self.playing_state = True
    def stop(self):
        mixer.music.stop()

root = Tk()
app = Mp3player(root)
root = mainloop() 

   

        
   

    