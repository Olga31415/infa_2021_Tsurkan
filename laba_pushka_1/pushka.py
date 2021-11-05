import math
from random import *
import pygame
import numpy as np


FPS = 30
player = input('Enter your name:')

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

timer = 0
points = 0

pygame.font.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

class Ball:
    def __init__(self, screen: pygame.Surface, x= 40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.g = -3
        self.timer = 300

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy += self.g
        self.timer -= 1
        if self.x - self.r < 0:
            self.vx = (-self.vx) * 0.8
            self.x = self.r
        elif self.x + self.r > 800:
            self.vx = (-self.vx) * 0.8
            self.x = 800 - self.r
        if self.y - self.r < 0:
            self.vy = -self.vy
            self.y = self.r
        elif self.y + self.r > 600:
            self.vy = (-self.vy) * 0.8 + self.g
            self.y = 600 - self.r

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2)


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.puska = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 40
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):

        pygame.draw.polygon(self.screen, self.color,
                            [(self.x + int(5 * np.cos(-self.an + 1.57)), self.y - int(5 * np.sin(-self.an + 1.57))),
                             (self.x + int(5 * np.cos(-self.an - 1.57)), self.y - int(5 * np.sin(-self.an - 1.57))),
                             (self.x + int(
                                 np.power((30 + self.f2_power / 2) * (30 + self.f2_power / 2) + 5 * 5, 0.5) * np.cos(
                                     -self.an - 5 / (30 + self.f2_power / 2))), self.y - int(
                                 np.power((30 + self.f2_power / 2) * (30 + self.f2_power / 2) + 5 * 5, 0.5) * np.sin(
                                     -self.an - 5 / (30 + self.f2_power / 2)))),
                             (self.x + int(
                                 np.power((30 + self.f2_power / 2) * (30 + self.f2_power / 2) + 5 * 5, 0.5) * np.cos(
                                     -self.an + 5 / (30 + self.f2_power / 2))), self.y - int(
                                 np.power((30 + self.f2_power / 2) * (30 + self.f2_power / 2) + 5 * 5, 0.5) * np.sin(
                                     -self.an + 5 / (30 + self.f2_power / 2))))])



    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target():

    def __init__(self, screen: pygame.Surface):
        """ Инициализация новой цели. """
        self.screen = screen
        self.x = randint(600, 780)
        self.y = randint(50, 550)
        self.r = randint(10, 50)
        self.color = RED
        self.points = 0
        self.live = 1
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        self.timer = 300


    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.x = randint(600, 780)
        self.y = randint(50, 550)
        self.r = randint(2, 50)
        self.color = RED
        self.live = 1
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)


    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x - self.r < 0:
            self.vx = -self.vx
            self.x = self.r
        elif self.x + self.r > 800:
            self.vx = -self.vx
            self.x = 800 - self.r
        if self.y - self.r < 0:
            self.vy = -self.vy
            self.y = self.r
        elif self.y + self.r > 600:
            self.vy = -self.vy
            self.y = 600 - self.r

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

class knopka:

    def __init__(self, screen):
        self.screen = screen
        self.x = 700
        self.y = 50
        self.w = 90
        self.h = 50
        self.color = RED

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.x, self.y, self.w, self.h))

    def down(self, event):
        x1, y1 = event.pos
        if 700 <= x1 <= 790 and 50 <= self.y <= 100:
            return True        


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []

for t in range(4):
    targets.append(Target(screen))

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False
play_time = 24000
button = knopka(screen)

while not finished:
    screen.fill(WHITE)
    gun.draw()
    button.draw()
    text_surface = font.render('your points: ' + str(points), True, (0, 0, 0))
    screen.blit(text_surface, (0, 0))
    timer += 1

    for b in balls:
        b.draw()
    for t in targets:
        t.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if pygame.time.get_ticks() >= play_time:
            finished = True        
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.down(event):
                play_time = 24000
                points = 0            
            gun.fire2_start(event)  # зарядка пушки
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)  # выстрел
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)  # слежка за мышкой


    for b in balls:
        b.move()
        if b.timer <= 0:
            balls.remove(b)
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                points += 1


    for t in targets:
        t.move()

    gun.power_up()
print('Nice work,', player, '! Your score ', points)
result = str((player, points))
f = open('шарики классы.txt', 'a')
f.write(result)
f.close()
pygame.quit()
