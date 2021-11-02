import math
from random import choice
import random as ran
import pygame


FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

name = input('Ваше имя: ')

g = - 1
t = 1

points = 0

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.g = 100
        self.vx = 5
        self.vy = 5
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (self.x < (800 - self.r) and  self.x > self.r):
            self.x += self.vx
            self.vx = self.vx * 0.99
        else:
            self.vx = - self.vx
            self.x = self.x + 2 * self.vx
            
        if (self.y < (600 - self.r) and  self.y > self.r):
            self.y += self.vy
            self.vy = self.vy - g*t
            self.vy = self.vy * 0.95
        else:
            self.vy = - 0.9*self.vy
            self.y = self.y + 0.9*self.vy
        

    def draw(self, screen):
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
        if abs(self.x - obj.x) <= self.r + obj.r and abs(self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.wigth=6
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        self.an = math.atan2((-event.pos[1]+new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = -math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, screen): 
        pygame.draw.polygon(self.screen, self.color, ([40, 450],
                                                      [40 + self.f2_power * math.cos(self.an), 450 - self.f2_power * math.sin(self.an)],
                                                      [40 + self.f2_power * math.cos(self.an) + self.wigth * math.sin(self.an), 450 - self.f2_power * math.sin(self.an) + self.wigth * math.cos(self.an)],
                                                      [40 + self.wigth * math.sin(self.an), 450 + self.wigth * math.cos(self.an)]))
        # FIXIT don't know how to do it
        

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.x = ran.randint(600, 780)
        self.y = ran.randint(300, 550)
        self.r = 10
        self.vx = 5
        self.vy = 5
        self.points = 1
        self.live = 100
        self.color = choice(GAME_COLORS)
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = ran.randint(600, 780)
        y = self.y = ran.randint(300, 550)
        r = self.r = ran.randint(2, 50)
        color = self.color = RED
        self.live = 1
        self.points = 1
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)
    

    def hit(self):
        """Попадание шарика в цель."""
        global points
        points = points + self.points
        self.live = 0
       

    def draw(self, screen):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move (self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > 800 - self.r or self.x < self.r:
            self.vx = - self.vx
        if self.y > 600 - self.r or self.y < self.r:
            self.vy = - self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
r = 10


clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
target1 = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw(screen)
    target.draw(screen)
    target.move()
    target1.draw(screen)
    target1.move()
    for b in balls:
        b.draw(screen)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            balls = []
            target.hit()
            target.new_target()
            target.draw(screen)
        if b.hittest(target1) and target1.live:
            balls = []
            target1.hit()
            target1.new_target()
            target1.draw(screen)
            
    gun.power_up()

print('Поздравляем, ваш счет:', points)

pygame.quit()

dict_rating={}

with open ('results.txt','a') as file:
    file.write(str(name) + ' ' + str(points) + '\n')

with open ('results.txt','r') as file:
    for line_row in file:
        if len(line_row) == 0:
            continue
        line = line_row.strip().split()
        dict_rating.update({line[0]: line[1]})
        dict_rating.items()
        sorted_tuple = sorted(dict_rating.items(), key = lambda x: x[1], reverse = True)
        dict_rating = dict(sorted_tuple)

with open ('results.txt','w') as inf:
        inf.writelines([key+' '+dict_rating[key]+'\n' for key in dict_rating.keys()])
