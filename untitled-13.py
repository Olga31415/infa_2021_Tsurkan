import numpy as np
import turtle

turtle.shape('turtle')
turtle.color('black', 'yellow')
turtle.begin_fill()
for i in range(360):
    turtle.left(1)
    turtle.forward(np.pi * 2 * 90 / 360)
turtle.end_fill()
turtle.penup()
turtle.goto(-30, 115)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
for i in range(360):
    turtle.left(1)
    turtle.forward(np.pi * 2 * 20 / 360)
turtle.end_fill()
turtle.penup()
turtle.goto(30, 115)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
for i in range(360):
    turtle.left(1)
    turtle.forward(np.pi * 2 * 20 / 360)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 110)
turtle.pendown()
turtle.right(90)
turtle.width(7)
turtle.forward(25)
turtle.penup()
turtle.goto(40, 85)
turtle.pendown()
turtle.color('red')
for i in range(180):
    turtle.right(1)
    turtle.forward(np.pi * 2 * 40 / 360)

