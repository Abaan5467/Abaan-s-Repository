import turtle 

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('white')
s.title('France Flag')

t.speed(10)

t.penup()
t.setpos(-235,-150)
t.pendown()

t.begin_fill()
t.fillcolor('red')

t.fd(150)
t.lt(90)
t.fd(350)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(350)
t.end_fill()
t.lt(90)
t.fd(150)
t.begin_fill()
t.fillcolor('white')
t.fd(150)
t.lt(90)
t.fd(350)
t.lt(90)
t.fd(150)
t.end_fill()
t.rt(180)
t.fd(150)
t.begin_fill()
t.fillcolor('blue')
t.fd(150)
t.rt(90)
t.fd(350)
t.rt(90)
t.fd(150)
t.end_fill()


turtle.done()
