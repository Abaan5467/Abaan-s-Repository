import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.penup()
t.setpos(0,90)
t.pendown()
t.speed(1000)
t.pensize(5)
colours = ['red','green','blue','orange','pink','cyan','white','purple','yellow']
while True:
    for x in colours:
        t.pencolor(x)
        t.circle(100)
        t.fd(10)
        t.rt(5)
turtle.done()