import numpy as np
import turtle
turtle.shape('turtle')
n = 3
R = 30
r = R / 2
for i in range(10):
    turtle.left(180 - 180 * (n - 2) /(2* n))
    for i in range(n):
        turtle.forward(R * 2 * np.sin(np.pi / (n)))
        turtle.left(180 - 180 * (n - 2) / n)
    turtle.right(180 - 180 * (n - 2) /(2* n))
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    n = n + 1
    R = R + r

