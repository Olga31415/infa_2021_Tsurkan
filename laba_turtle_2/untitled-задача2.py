import turtle
import random as rnd
import numpy as np
n = input()

x = 35
y = 0

for i in n:
    a =int(i)
    if a == 0:  # ��� ����
        zero = [(25, 90), (50, 90), (25, 90), (50, 90)]
        for st, gr in zero:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 1:  # ��� �������
        turtle.right(90)
        turtle.penup()
        turtle.forward(25)
        turtle.left(135)
        turtle.pendown()
        one = [(25 * 2**0.5, 135), (50, 270)]
        for st, gr in one:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 2:  # ��� ������
        two = [(25, 90), (25, 45), (25 * 2**0.5, 135), (25, 0)]
        for st, gr in two:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 3:  # ��� ������
        tree = [(25, 135), (25 * 2**0.5, 135), (25, 135), (25 * 2**0.5, 135)]
        for st, gr in tree:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 4:  # ��� ��������
        turtle.right(90)
        four = [(25, 90), (25, 270), (25, 180), (50, 270)]
        for st, gr in four:
            turtle.forward(st)
            turtle.left(gr)
    elif a == 5:  # ��� �������
        five = [(25, 180), (25, 90), (25, 90),
                 (25, 270), (25, 270), (25, 180)]
        for st, gr in five:
            turtle.forward(st)
            turtle.left(gr)
    elif a == 6:  # ��� ��������
        turtle.penup()
        turtle.forward(25)
        turtle.right(135)
        turtle.pendown()
        six = [(25 * 2**0.5, 45), (25, 90), (25, 90),
                 (25, 90), (25, 180)]
        for st, gr in six:
            turtle.forward(st)
            turtle.left(gr)
    elif a == 7:  # ��� �������
        seven = [(25, 135), (25 * 2**0.5, 360 - 45), (25, 270)]
        for st, gr in seven:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 8:  # ��� ���������
        eight = [(25, 90), (25,90), (25, 270), (25,180),(50,180),(50,270),(25,270),(25,90)]
        for st, gr in eight:
            turtle.forward(st)
            turtle.right(gr)
    elif a == 9:  # ��� �������
        turtle.right(90)
        nine = [(25, 90), (25, 225), (25 * 2**0.5, 180), (25 * 2**0.5, 45),
                 (25, 90), (25, 180)]
        for st, gr in nine:
            turtle.forward(st)
            turtle.left(gr)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 35














