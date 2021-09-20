import numpy as np
import turtle

turtle.shape('turtle')
turtle.left(90)
a = 30
for i in range(10):
    for i in range(360):
        turtle.left(1)
        turtle.forward(np.pi * 2 * a / 360)
    for i in range(360):
        turtle.right(1)
        turtle.forward(np.pi * 2 * a / 360)
    a=a+10