import turtle
import numpy as np


turtle.shape("circle")
v = 20
a = 70
a = a * np.pi / 180
ax = 0
ay = -1
ky=-0.01
vx = v * np.cos(a)
vy = v * np.sin(a)
dt = 0.1
x = 0
y = 0
turtle.goto(400, 0)
turtle.goto(-400, 0)
x = -400
for i in range(10000):
    vx = vx + ax * dt
    x = x + vx * dt
    y = y + vy * dt
    vy = vy + ay * dt + ky * vy * dt
    if y <= 0:
        vy = - vy
    turtle.goto(x, y)
    
    
    
    
    