import turtle
import numpy as np

turtle.shape('turtle')
for i in range(360):
    turtle.left(1)
    turtle.forward(np.pi * 2 * 40 / 360)