import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()


FPS = 60
screen = pygame.display.set_mode((600, 600))

player = input('Enter your name:')

""" создаем массив цветов, используемых в игре"""
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

"""создаем класс krug. задаем рандомно параметры шариков и их скорости. 
с помощью popal определяем попадание или промах по шарику. dvizh описывает характер движения шариков."""
class krug:
    def __init__(self):
        self.new()

    def new(self):
        self.x = randint(100, 500)
        self.y = randint(100, 500)
        self.r = randint(10, 60)
        self.color = COLORS[randint(0, 5)]
        self.Vx, self.Vy = randint(-3, 3), randint(-3, 3)

    def draw(self, scr=screen):
        circle(scr, self.color, (self.x, self.y), self.r)
    def dvizh(self):
        if self.x - self.r <= 0:
            self.Vx *= -1
        if self.x + self.r >= 600:
            self.Vx *= -1
        if self.y - self.r <= 0:
            self.Vy *= -1
        if self.y + self.r >= 600:
            self.Vy *= -1

        self.x += self.Vx
        self.y += self.Vy

    def popal(self, sob):
        x1, y1 = sob.pos
        R = np.sqrt((x1 - self.x)**2 + (y1 - self.y)**2)
        return R <= self.r

""" pryamougol класс объектов прямоугольников. рандомно задаютмя параметры прямоугольников.
dvizh описывает характер движения шариков, popal характиристики попадания по мишени
или промаха"""
class pryamougol:
    def __init__(self):
        self.new()

    def new(self):
        self.x = randint(100, 500)
        self.y = randint(100, 500)
        self.ry, self.rx = randint(10, 60), randint(10, 60)
        self.color = COLORS[randint(0, 5)]
        self.Vx, self.Vy = randint(-3, 3), randint(-3, 3)

    def draw(self, scr=screen):
        rect(scr, self.color, (self.x, self.y, self.rx, self.ry))
    def dvizh(self):
        if self.x <= 0:
            self.Vx *= -1
        if self.x + self.rx >= 600:
            self.Vx *= -1
        if self.y <= 0:
            self.Vy *= -1
        if self.y + self.ry >= 600:
            self.Vy *= -1

        self.x += self.Vx
        self.y += self.Vy

    def popal(self, sob):
        x1, y1 = sob.pos
        return (x1 - self.x <= self.rx) and (y1 - self.y <= self.ry) and (x1 - self.x >= 0) and ((y1 - self.y >= 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
play_time = 60000

""" задаем количество объектов различных классов"""
number_of_sf = 2
number_of_kr = 7

sfery = [krug() for _ in range(number_of_sf)]
pr = [pryamougol() for _ in range(number_of_kr)]
S = 0

""" если есть нажатие мышки: в случае попадания в круг, появляется новый и начисляется 1 балл;
в случае попадания в прямоугольник, появляется новый и начисляется 5 баллов"""
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    if pygame.time.get_ticks() >= play_time:
        finished = True    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sfera in sfery:
                if sfera.popal(event) == True:
                    S += 1
                    print(S)
                    sfera.new()
            for pr1 in pr:
                if pr1.popal(event) == True:
                    S += 5
                    print(S)
                    pr1.new()
    for pr1 in pr:
        pr1.dvizh()
        pr1.draw()

    for sfera in sfery:
        sfera.dvizh()
        sfera.draw()

    pygame.display.update()
print('Nice work,', player, '! Your score ', S)
result = str((player, S))
f = open('шарики классы.txt', 'a')
f.write(result)
f.close()
pygame.quit()
