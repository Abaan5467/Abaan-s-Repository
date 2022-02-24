from tkinter import * 
import time
frame = Tk()
frame.title('Bouncing ball')
w=500
h=400
cv=Canvas(frame,width=w,height=h)
cv.pack()
ball=cv.create_oval(10,10,60,60,fill='cyan')
ball2=cv.create_oval(12,12,60,60,fill='red')
xspd=1
yspd=2
xspd1=2
yspd1=3
while True:
    cv.move(ball,xspd,yspd)
    cv.move(ball2,xspd1,yspd1)
    cd=cv.coords(ball)
    cd2=cv.coords(ball2)
    if cd[3]>=400 or cd[1]<=0:
        yspd=-yspd
    if cd2[3]>=400 or cd2[1]<=0:
        yspd1=-yspd1
               
    if cd2[2]>=200 or cd2[0]<=0:
        xspd1=-xspd1

    if cd[2]>=200 or cd[0]<=0:
        xspd=-xspd
    frame.update()
    frame.update()
    time.sleep(0.01)
frame.mainloop()
    


