import numpy as np
import turtle
n=int(input())
turtle.shape('turtle')
turtle.left(180)
for i in range(n):
    turtle.forward(100)
    turtle.left(180 - 180 / n)    

