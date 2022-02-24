from tkinter import * 
import pywhatkit
frame = Tk()
frame.title('Most Dangerous Design')
frame.geometry("500x400")
def redirect():
    pywhatkit.playonyt("https://www.youtube.com//watch?v=xvFZjo5PgG0")
btn = Button(frame,text="Click at your own risk",command=redirect)
btn.grid(row=0,column=0)

frame.mainloop()