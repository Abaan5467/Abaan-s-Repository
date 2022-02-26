from tkinter import * 
from time import sleep
frame = Tk()
frame.title('Canvas')
frame.geometry('500x500')
w=500
h=500
cv=Canvas(frame,width=w,height=h)
cv.pack()
ball = cv.create_oval(150,150,65,60,fill='red')
xspd = 15
yspd = 25
while True:
    cv.move(ball,xspd,yspd)
    frame.update()
    sleep(0.1)
    cord = cv.coords(ball)
    if cord[0]<=0 or cord[2]>=w:
        xspd=-xspd
    if cord[1]<=0 or cord[3]>=h:
        yspd=-yspd
#[65.0, 60.0, 150.0, 150.0]
frame.mainloop()
