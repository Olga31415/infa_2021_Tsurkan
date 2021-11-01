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
i = 0


''' функция new_ball создает параметры для новых шариков'''
def new_ball() :
        x = randint(100, 500)
        y = randint(100, 500)
        r = randint(10, 60)
        color = COLORS[randint(0, 5)]
        Vx, Vy = randint(-3, 3), randint(-3, 3)
        return [x, y, r, Vx, Vy, color]

''' функция draw рисует новыешарики'''
def draw(sfera, scr=screen):
        circle(scr, sfera[5], (sfera[0], sfera[1]), sfera[2])

''' dvizh описывает движение шариков и столкновения'''
def dvizh(sfera, scr=screen):
        if sfera[0] - sfera[2] <= 0:
                sfera[3] *= -1
        if sfera[0] + sfera[2] >= 600:
                sfera[3] *= -1
        if sfera[1] - sfera[2] <= 0:
                sfera[4] *= -1
        if sfera[1] + sfera[2] >= 600:
                sfera[4] *= -1
        sfera[0] += sfera[3]
        sfera[1] += sfera[4]
        return sfera

''' popal описывает событие попадания, возвращает правду/ложь события и счетчк i, которая отчитывает номер шарика'''
def popal(event):
        global sfera, temp
        for sfera in sfery:
                x1, y1 = event.pos
                if (x1 - sfera[0])**2 + (y1 - sfera[1])**2 <= sfera[2]**2:
                        temp = ((x1 - sfera[0])**2 + (y1 - sfera[1])**2 <= sfera[2]**2)
                        sfery.remove(sfera)
                        sfery.append(new_ball())
                        return temp


pygame.display.update()
clock = pygame.time.Clock()
finished = False
play_time = 60000


''' создвем массив шаров'''
number_of_sf = 5
sfery = [new_ball() for _ in range(number_of_sf)]
S = 0

while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        if pygame.time.get_ticks() >= play_time:
                finished = True    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if popal(event) == True:
                                i += 1
                                print(i)

                                                                
        for sfera in sfery:
                dvizh(sfera, scr=screen)
                draw(sfera, scr=screen)
        pygame.display.update()
print('Nice work,', player, '! Your score ', S)
result = str((player, S))
f = open('шарики классы.txt', 'a')
f.write(result)
f.close()
pygame.quit()
