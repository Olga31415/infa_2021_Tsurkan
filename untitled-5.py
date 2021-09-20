import numpy as np
import turtle
x = -5
y = -5
turtle.shape('turtle')
for i in range(30, 121, 10):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.goto(x, y)
    x = x - 5
    y = y - 5
    turtle.left(90)
    turtle.pendown()









