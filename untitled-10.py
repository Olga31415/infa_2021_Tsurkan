import numpy as np
import turtle

turtle.shape('turtle')
for a in range(3):
    for i in range(360):
        turtle.left(1)
        turtle.forward(np.pi * 2 * 30 / 360)
    for i in range(360):
        turtle.right(1)
        turtle.forward(np.pi * 2 * 30 / 360)
    turtle.left(60)
    
    




