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
PINK = (255, 20, 147)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#размеры экрана
WIDTH = 800
HEIGHT = 600
tank_size = 100
l = 0 #счетчик очков
p = str (l)

tank_image = pygame.image.load('tank.png')
tank_image = pygame.transform.scale(tank_image, (tank_size, tank_size))

bomba_pikch = pygame.image.load('bomba.png')
bomba_pikch = pygame.transform.scale(bomba_pikch, (50, 50))

name = input('Ваше имя: ')

g = - 1
t = 1

points = 0

class Bomba:
    def __init__(self, screen):
        """ Конструктор класса Bomba """
        self.screen = screen
        self.size = 10
        self.x = ran.randint(self.size, WIDTH - self.size)
        self.y = 0
        self.life = 1
        self.vy = 5

    def new_bomba(self):
        """Инициализация новой бомбы"""
        x = self.x = ran.randint(self.size, WIDTH  - self.size)
        self.y = 0
        self.life = 1
        self.vy = 5
        
    def move(self, obj):
        """Движение бомбы"""
        self.y += self.vy

    def end_life(self):
        return (HEIGHT < self.y)
    
    def draw(self):
        """Прорисовка бомбы"""
        self.screen.blit(bomba_pikch, (self.x, self.y))

    def hittest(self, obj):
        """Проверка стоклновения бомбы с танком: минус жизнь"""
        return (((self.y + self.size) > obj.y) and (self.y < (obj.y + obj.size)) and ((self.x + self.size) > obj.x) and (self.x < (obj.x + obj.size)))

class Ball:
    def __init__(self, screen):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 40
        self.y = 450
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
        
class Ball_2 (Ball):

    def __init__ (self, screen):
        super().__init__(screen)


    def draw_ball2(self, screen):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x, self.y, self.r, self.r))
        
    
    

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.x = 40
        self.y = 420
        self.f2_power = 10
        self.f2_on = 0
        self.wigth= 6
        self.an = 1
        self.color = GREY
        self.speed = 12
        self.size = tank_size

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_left_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.x = self.x + 60
        new_ball.y = self.y
        self.an = math.atan2((-event.pos[1]+new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def fire2_right_end(self, event):
        """Выстрел другим снарядом

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global rects, bullet
        bullet += 1
        new_ball = Ball_2(self.screen)
        new_ball.x = self.x + 60
        new_ball.y = self.y 
        self.an = math.atan2((-event.pos[1]+new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        rects.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = -math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = PINK
        else:
            self.color = BLACK

    def draw_tank(self, screen):
        self.screen.blit(tank_image, (self.x, self.y))

    def move_tank(self, pressed, screen):
        if pressed[pygame.K_RIGHT]:
            self.x = self.x + self.speed
        if pressed[pygame.K_LEFT]:
            self.x = self.x - self.speed
        if pressed[pygame.K_UP]:
            self.y = self.y - self.speed
        if pressed[pygame.K_DOWN]:
            self.y = self.y + self.speed
            
        
    

    '''def draw(self, screen): 
        pygame.draw.polygon(self.screen, self.color, ([self.x, self.y + 30],
                                                      [self.x + self.f2_power * math.cos(self.an), self.y + 30 - self.f2_power * math.sin(self.an)],
                                                      [self.x + self.f2_power * math.cos(self.an) + self.wigth * math.sin(self.an), self.y + 30 - self.f2_power * math.sin(self.an) + self.wigth * math.cos(self.an)],
                                                      [self.x + self.wigth * math.sin(self.an), self.y + 30 + self.wigth * math.cos(self.an)]))'''

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = PINK
        else:
            self.color = BLACK


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
        """Прорисовка цели"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move (self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > 800 - self.r or self.x < self.r:
            self.vx = - self.vx
        if self.y > 600 - self.r or self.y < self.r:
            self.vy = - self.vy
            
class Target_2 (Target):

    def __init__ (self, screen):
        super().__init__(screen)

    def draw_rect(self, screen):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.r, self.r))

    def move_rect (self):
        self.x = self.x + self.vx
        self.y = 100 * math.sin(self.x * 50) + self.y
        if self.x > 800 - self.r or self.x < self.r:
            self.vx = - self.vx
        if self.y > 600 - self.r or self.y < self.r:
            self.vy = - self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
rects = []
r = 10





clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
target1 = Target_2(screen)
bomba = Bomba(screen)
bomba.new_bomba()
finished = False

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков: ', True,
                  (180, 180, 0))

while not finished:
    screen.fill(WHITE)
    
    gun.draw_tank(screen)

    
    bomba.draw()
    bomba.move(bomba)
    
    target.draw(screen)
    target.move()
    
    target1.draw_rect(screen)
    target1.move_rect()
    
    for b in balls:
        b.draw(screen)

    for r in rects:
        r.draw_ball2(screen)

    screen.blit(text1, (10, 50))
    text2 = f1.render(p, True,
                      (180, 180, 0))
    screen.blit(text2, (300, 50))
    
        
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        massiv_klavish = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            gun.fire2_left_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            gun.fire2_right_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        if massiv_klavish:
            gun.move_tank(massiv_klavish, screen)
            
    if bomba.hittest(gun) or bomba.end_life():
        bomba.new_bomba()



    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            balls = []
            target.hit()
            target.new_target()
            target.draw(screen)
            l = l + 1
            p = str (l)
        if b.hittest(target1) and target1.live:
            balls = []
            target1.hit()
            target1.new_target()
            target1.draw(screen)
            l = l + 1
            p = str (l)

    for r in rects:
        r.move()
        if r.hittest(target) and target.live:
            rects = []
            target.hit()
            target.new_target()
            target.draw(screen)
            l = l + 1
            p = str (l)
        if r.hittest(target1) and target1.live:
            rects = []
            target1.hit()
            target1.new_target()
            target1.draw(screen)
            l = l + 1
            p = str (l)

    

    pygame.display.update()


    
    gun.power_up()

print('Поздравляем, ваш счет:', points)

pygame.quit()

#создание файла с результатами
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
