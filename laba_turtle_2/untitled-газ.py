from random import randint
import turtle


number_of_turtles = 6
steps_of_time_number = 100000

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(400)
turtle.right(90)


pool = [[turtle.Turtle(shape='circle'), 0, 0, 0, 0]
                       for i in range(number_of_turtles)]

for unit in pool:
    unit[0].penup()
    x = randint(-200, 200)
    y = randint(-200, 200)

    unit[1], unit[2] = x, y

    Vx, Vy= randint(-10,10), randint(-10,10)
    unit[3], unit[4] = Vx, Vy
    
    unit[0].goto(x, y)



for i in range(steps_of_time_number):
    for unit in pool:
        unit[0].goto(unit[1], unit[2])
        unit[1] += unit[3]
        unit[2] += unit[4]

        if abs(unit[1]) >= 200:
            unit[3] = -unit[3]
        if abs(unit[2]) >= 200:
            unit[4]=-unit[4]
            

