import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
grey = (230, 230, 230)
screen.fill(grey)

circle(screen, (255, 255, 51), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)

rect(screen, (0, 0, 0), (150, 250, 100, 13))

circle(screen, (255, 0, 0), (155, 160), 24)
circle(screen, (0, 0, 0), (155, 160), 10)
circle(screen, (255, 0, 0), (250, 160), 19)
circle(screen, (0, 0, 0), (250, 160), 10)

polygon(screen, (0, 0, 0,), ([179, 148], [184, 143], [131, 124], [136, 119]))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()