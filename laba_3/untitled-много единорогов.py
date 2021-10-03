import pygame
from pygame.draw import *

pygame.init()

sr1 = pygame.Surface((200, 360))
sr1.fill((0, 0, 0))
sre = pygame.Surface((400, 400))
sre.fill((0, 0, 0))
sre.set_colorkey((0, 0, 0))

FPS = 30
screen = pygame.display.set_mode((600, 1000))

rect(screen, (0, 255, 255), (0, 0, 600, 450))
rect(screen, (0, 255, 0), (0, 450, 600, 550))

r = 0
g = 255
b = 255
R = 90
for i in range(255):
    circle(screen, (r, g, b), (550, 200), R)
    b -= 1
    r += 1
    R -= 0.5

rect(sr1, (231, 231, 231), (85, 210, 30, 150))  # дерево
ellipse(sr1, (0, 129, 0), (35, 0, 130, 145))
ellipse(sr1, (0, 255, 0), (35, 0, 130, 145), 1)
ellipse(sr1, (0, 129, 0), (0, 60, 200, 85))
ellipse(sr1, (0, 255, 0), (0, 60, 200, 85), 1)
ellipse(sr1, (0, 129, 0), (40, 127, 120, 85))
ellipse(sr1, (0, 255, 0), (40, 127, 120, 85), 1)
circle(sr1, (255, 205, 171), (20, 105), 13)
circle(sr1, (255, 205, 171), (170, 107), 13)
circle(sr1, (255, 205, 171), (140, 170), 13)
circle(sr1, (255, 205, 171), (80, 70), 13)

sr1.set_colorkey((0, 0, 0))

sr2=pygame.transform.rotozoom(sr1, 0, 1.05)
sr2.set_colorkey((0, 0, 0))
screen.blit(sr2, (-20, 260))
screen.blit(sr1, (30, 220))
screen.blit(sr1, (-15, 320))
sr2=pygame.transform.scale(
    sr1, (sr1.get_width() // 2, sr1.get_width() // 1))
sr2=pygame.transform.flip(sr2, 150, 0)
screen.blit(sr2, (200, 320))


ellipse(sre, (255, 255, 255), (70, 200, 200, 100))  # тело и ноги
rect(sre, (255, 255, 255), (90, 280, 20, 90))
rect(sre, (255, 255, 255), (125, 280, 20, 80))
rect(sre, (255, 255, 255), (200, 280, 20, 90))
rect(sre, (255, 255, 255), (230, 280, 20, 80))

ellipse(sre, (255, 255, 255), (200, 110, 70, 165))  # голова
ellipse(sre, (255, 255, 255), (230, 105, 85, 43))
circle(sre, (230, 129, 171), (260, 120), 9)
circle(sre, (0, 0, 1), (258, 118), 4)
polygon(sre, (234, 177, 176), ([225, 113], [235, 5], [245, 113]))

ellipse(sre, (222, 177, 234), (185, 110, 65, 20))  # грива
ellipse(sre, (222, 177, 234), (183, 112, 65, 20))
ellipse(sre, (255, 239, 171), (182, 125, 60, 18))
ellipse(sre, (255, 239, 171), (162, 165, 55, 23))
ellipse(sre, (244, 216, 228), (172, 145, 52, 23))
ellipse(sre, (176, 234, 222), (150, 175, 52, 23))
ellipse(sre, (234, 177, 176), (150, 185, 55, 20))
ellipse(sre, (234, 177, 176), (180, 135, 60, 23))

ellipse(sre, (234, 177, 176), (55, 215, 60, 23))  # хвост
ellipse(sre, (214, 177, 176), (45, 220, 55, 20))
ellipse(sre, (255, 239, 171), (0, 270, 63, 30))
ellipse(sre, (222, 177, 234), (35, 250, 65, 20))
ellipse(sre, (255, 239, 171), (40, 260, 60, 18))
ellipse(sre, (255, 239, 171), (35, 227, 55, 23))
ellipse(sre, (244, 216, 228), (10, 240, 62, 33))
ellipse(sre, (176, 234, 222), (35, 270, 32, 23))
ellipse(sre, (200, 177, 176), (40, 280, 60, 23))
ellipse(sre, (176, 234, 222), (45, 270, 55, 23))


sre1=pygame.transform.rotozoom(sre, 0, 0.3)
sre1=pygame.transform.flip(sre1, 150, 0)
sre1.set_colorkey((0, 0, 0))
screen.blit(sre1, (350, 350))
sre1=pygame.transform.rotozoom(sre, 0, 0.45)
sre1=pygame.transform.flip(sre1, 150, 0)
sre1.set_colorkey((0, 0, 0))
screen.blit(sre1, (420, 370))
sre1=pygame.transform.rotozoom(sre, 0, 0.6)
sre1.set_colorkey((0, 0, 0))
screen.blit(sre1, (220, 350))
screen.blit(sre, (200, 405))

pygame.display.update()
clock=pygame.time.Clock()
finished=False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()