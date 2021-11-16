
import math
from random import *
import pygame
import numpy as np


FPS = 30
player1 = input('Enter your name:')
player2 = input('Enter your name:')
d_an = 15 * 3.14 / 180

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
    def __init__(self, number, screen: pygame.Surface, x=40, y=450):
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
        self.who = number

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
        """сталкивание с мишенями круглой формы"""
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2)

    def hittest1(self, obj):
        """сталкивание с мишенями прямоцгольной формы"""
        if (obj.x + self.r <= self.x <= obj.x + obj.rx + self.r) and (obj.y + self.r <= self.y <= obj.y + obj.ry + self.r):
            return True

    def hittest2(self, obj):
        """сталкивание с другими танками, не с "материнским"""
        if obj.num != self.who:
            x_lev_verh = obj.x1
            y_lev_verh = obj.y
            if x_lev_verh + self.r <= self.x <= x_lev_verh + 100 + self.r and y_lev_verh - 5 + self.r <= self.y <= y_lev_verh + 45 + self.r:
                obj.live -= 1
                return True
        

class Gun:
    def __init__(self, num, screen):
        """задаем параметры пушки"""
        self.screen = screen
        self.puska = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 100
        self.y = 450
        self.vx = 2
        self.live = 10
        self.num = num

    def fire2_start(self, event):
        """зарядка пушки"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.num, self.screen, self.x, self.y)
        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def up(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an += d_an
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def down(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an -= d_an
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY







    def draw(self):
        """ отрисовка самой пушки и частей танка"""
        pygame.draw.polygon(self.screen, self.color,
                            [(self.x + int(5 * np.cos(-self.an + 1.57)), self.y - int(5 * np.sin(-self.an + 1.57))),
                             (self.x + int(5 * np.cos(-self.an - 1.57)),
                              self.y - int(5 * np.sin(-self.an - 1.57))),
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
        self.x1, self.y1 = self.x - 50, 460
        self.x2, self.y2 = self.x - 10, 445
        pygame.draw.rect(screen, GREY,
                         (self.x1, self.y1, 100, 30))
        pygame.draw.rect(screen, GREY,
                         (self.x2, self.y2, 30, 15))



    def power_up(self):
        """что происходит во время зарядки"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    """движение в зависимости от того какая кнопка зажата"""
    def move11(self, event):
        self.x += self.vx

    def move12(self, event):
        self.x -= self.vx
    


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
        """ характер движения целей"""
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

class pryamougol:
    
    def __init__(self, screen: pygame.Surface):
        """ Инициализация новой цели. """
        self.x = randint(100, 500)
        self.y = randint(100, 380)
        self.ry, self.rx = randint(10, 60), randint(10, 60)
        self.color = BLUE
        self.points = 0
        self.live = 1        
        self.vx, self.vy = randint(-3, 3), randint(-3, 3)
        self.ax, self.ay = 0.3, 0.3
        
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.x = randint(100, 500)
        self.y = randint(100, 380)
        self.ry, self.rx = randint(10, 60), randint(10, 60)
        self.color = BLUE
        self.live = 1
        self.vx, self.vy = randint(-3, 3), randint(-3, 3)
        self.ax, self.ay = 0.3, 0.3
        
    def move(self):
        """описание характера движения"""
        self.x += self.vx
        self.y -= self.vy
        self.vx += self.ax
        self.vy -= self.ay
        if self.x <= 0:
            self.vx *= -1
        if self.x + self.rx >= 800:
            self.vx *= -1
        if self.y <= 0:
            self.vy *= -1
        if self.y + self.ry >= 400:
            self.vy *= -1

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.rx, self.ry))
        

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

class bomb:

    def __init__(self, screen):
        """инициация бомбы"""
        self.screen = screen
        self.x = randint(10,790)
        self.y = 10
        self.r = 10
        self.color = GREEN
        self.vy = 1
        self.points = 0
        self.live = 1         
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """характер движения"""
        self.y += self.vy
        self.vy += 0

    def hit(self):
        pass

    def hittest(self, obj):
        """попадание в танк"""
        if obj.x1 + self.r <= self.x <= obj.x1 + 100 + self.r and obj.y - 5 + self.r <= self.y <= obj.y + 45 + self.r:
            return True

        
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
bullet=0
balls = []
balls = []
targets = []
pryamougols = []
bombs = [bomb(screen)]

for t in range(4):
    targets.append(Target(screen))
for p in range(2):
    pryamougols.append(pryamougol(screen))

clock = pygame.time.Clock()
gun1 = Gun(1, screen)
gun2 = Gun(2, screen)
gun2.x = 700
button = knopka(screen)
finished = False
play_time = 20000

while not finished:
    screen.fill(WHITE)
    gun1.draw()
    gun2.draw()
    button.draw()
    text_surface = font.render(
        'your points: ' + str(points), True, (0, 0, 0))
    screen.blit(text_surface, (0, 0))
    timer += 1

    for b in balls:
        b.draw()
    for t in targets:
        t.draw()
    for p in pryamougols:
        p.draw()
    for bom in bombs:
        bom.draw()
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
                gun1.live = 10
                gun2.live = 10
                for t in targets:
                    t.draw()
                for p in pryamougols:
                    p.draw()            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            gun1.fire2_start(event)  # зарядка танка 1
        elif event.type == pygame.KEYUP and event.key == pygame.K_c:
            gun1.fire2_end(event)  # выстрел танк 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            gun2.fire2_start(event)  # зарядка танка 2
        elif event.type == pygame.KEYUP and event.key == pygame.K_l:
            gun2.fire2_end(event)  # выстрел танк 2
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            gun1.up(event)  # танк 1 вверх
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            gun1.down(event)  # танк 1 вниз
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            gun2.up(event)  # танк 2 вверх
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            gun2.down(event)  # танк 2 вниз
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            gun1.move11(event)  # 1танк в право
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            gun1.move12(event)  # 1танк в лево
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            gun2.move11(event)  # 2танк в право
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            gun2.move12(event)  # 2танк в лево



    for b in balls:
        b.move()
        if b.timer <= 0:
            balls.remove(b)
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                if b.who == 1:
                    points += 1
                elif b.who == 2:
                    points -= 1
        for pryamougo in pryamougols:
            if b.hittest1(pryamougo) and pryamougo.live:
                pryamougo.live = 0
                pryamougo.hit()
                if b.who == 1:
                    points += 3
                elif b.who == 2:
                    points -= 3
        if b.hittest2(gun1):
            points += 0.5
            if gun1.live == 0:
                finished = True
        elif b.hittest2(gun1):
            points -= 0.5
            if gun1.live == 0:
                finished = True            
        for bom in bombs:
            if b.hittest(bom) and bom.live:
                bom.live = 0
                if b.who == 1:
                    points += 5
                elif b.who == 2:
                    points -= 5
                bombs.remove(bom)

    if timer % 150 == 0:
        bombs.append(bomb(screen))
        
    for bom in bombs:
        if bom.hittest(gun1):
            gun1.live -= 1
            bombs.remove(bom)
            if gun1.live == 0:
                finished = True
                print('game over')

    for t in targets:
        for t in targets:
            t.move()        
        for p in pryamougols:
            p.move()
        for b in bombs:
            b.move()
    gun1.power_up()
    gun2.power_up()
if points <= 0:
    player = player2
elif points > 0:
    player = player1
print('Nice work,', player, '! You are win! Your score ', points)
result = str((player, points))
f = open('шарики классы.txt', 'a')
f.write(result)
f.close()
pygame.quit()
