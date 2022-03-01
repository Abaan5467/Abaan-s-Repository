import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('white')
t.penup()
t.setpos(0,90)
t.pendown()
t.shape('arrow')
t.speed(100)
while True:
    t.circle(150)
    t.fd(5)
    t.rt(3)

turtle.done()