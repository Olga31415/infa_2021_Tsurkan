import turtle
import numpy as np

turtle.shape('turtle')
turtle.left(90)
for j in range(40):
    for i in range(180):
        turtle.right(1)
        turtle.forward(np.pi * 2 * 30 / 360)
    for i in range(180):
        turtle.right(1)
        turtle.forward(np.pi * 2 * 5 / 360)




    
   

