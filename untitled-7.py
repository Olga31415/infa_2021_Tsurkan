import numpy as np
import turtle
n = 1
m = 0.1
turtle.shape('turtle')
for i in range(1000):
     turtle.left(n)
     turtle.forward(2 * np.pi * (m) / 360)
     m = m + 0.1
