from tkinter import *
from pyparsing import col
from pywhatkit.whats import sendwhatmsg

frame = Tk()
frame.geometry('800x500')
frame.title('Whatsapp')

def data():
    pn = phone_number.get()
    t = time.get()
    msg = message.get()
    x = t.split(':')
    hours = int(x[0])
    mins = int(x[1])
    sendwhatmsg(pn,msg,hours,mins,2)
    print('Message Sent')

lb = Label(frame,text='Enter the phone number with the calling code')
lb.grid(row=0,column=0)
phone_number = Entry(frame,width=30)
phone_number.grid(row=0,column=1)

lb2 = Label(frame,text='Enter the time at which you want to send the message in 24 hour format')
lb2.grid(row=1,column=0)
time = Entry(frame,width=30)
time.grid(row=1,column=1)

lb3 = Label(frame,text='Enter the message')
lb3.grid(row=2,column=0)
message = Entry(frame,width=30)
message.grid(row=2,column=1)

btn = Button(frame,text='Send',command=data)
btn.grid(row=3,column=0)
frame.mainloop()
