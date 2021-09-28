import turtle
import random as rnd
import numpy as np
n = input()
b = []
with open('xth.txt') as file:
    b = file.readlines()
x, y = [int(s) for s in b[0].split()]


for i in n:
    a = int(i)

    zero = [s for s in b[a + 1].split(', ')]
    for k in zero:
        st, gr, cl = [float(s) for s in k[1:-1].split(',')]
        if cl == 0:
            turtle.penup()
        elif cl == 1:
            turtle.pendown()
        turtle.forward(st)
        turtle.left(gr)
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 35



