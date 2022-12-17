from  tkinter.filedialog import askdirectory
from tkinter import *
import os
import pygame

frame = Tk()
frame.title('Music Player')
frame.geometry('500x500')
frame.resizable(0,0)
lb = Listbox(frame,bg='black',fg='white',width=55)
lb.pack()
songlist=[]

class musicplayer:
    def playsong(self):
        self.x = 0
        folder = askdirectory()
        os.chdir(folder)
        for songs in os.listdir(folder):
            if songs.endswith('.mp3') and songs not in songlist:
                songlist.append(songs)
            pygame.mixer.init()
            pygame.mixer.music.load(songlist[self.x])
            pygame.mixer.music.play()
        for y in songlist:
            lb.insert(len(songlist)-1,y)
        lb.itemconfig(self.x,{'bg':'blue'})    

    def pause(self):
        pygame.mixer.music.pause()
    def unpause(self):
        pygame.mixer.music.unpause()
    def next(self):
        lb.itemconfig(self.x,{'bg':'black'})    
        self.x+=1
        pygame.mixer.music.load(songlist[self.x])
        pygame.mixer.music.play()
        lb.itemconfig(self.x,{'bg':'blue'})    
    def prev(self):
        lb.itemconfig(self.x,{'bg':'black'})    
        self.x-=1
        pygame.mixer.music.load(songlist[self.x])
        pygame.mixer.music.play()
        lb.itemconfig(self.x,{'bg':'blue'})    
    def stop(self):
        frame.destroy()

player = musicplayer()
play= Button(frame,text='Open folder',padx=9,command=player.playsong)
play.pack()
pausebutton= Button(frame,text='Pause',padx=25,command=player.pause)
pausebutton.pack()
resume= Button(frame,text='Resume',padx=19,command=player.unpause)
resume.pack()
nxt = Button(frame,text='Next',padx=28,command=player.next)
nxt.pack()
previous = Button(frame,text='Previous',padx=18,command=player.prev)
previous.pack()
stp = Button(frame,text='Stop',padx=28,command=player.stop)
stp.pack()

frame.mainloop()