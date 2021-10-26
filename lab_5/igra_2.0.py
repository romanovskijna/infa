import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 80
A = 1200
B = 800
screen = pygame.display.set_mode((A, B))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

name = input('Ваше имя: ')
M = []
S = []

class Bublik:

    def __init__(self, screen):
        self.x = randint(100, 1100)
        self.y = randint(100, 700)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        self.Vx = randint(-100, 100) / 20
        self.Vy = randint(-100, 100) / 20

    def draw_bublik (self, screen):
        circle(screen, self.color, (self.x, self.y), self.r, round(self.r/4))

    def move_bublik(self, screen):
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        if self.x > A - self.r or self.x < self.r:
            self.Vx = - self.Vx
        if self.y > B - self.r or self.y < self.r:
            self.Vy = - self.Vy

    def control_bublik(self, screen, l):
        if (P[0] - self.x)**2 + (P[1] - self.y)**2 <= self.r**2 and (P[0] - self.x)**2 + (P[1] - self.y)**2 >= round(self.r*3/4)**2:
            self.r = 0
            l = l + 2
            print ('UUUUUURRRRRAAAAAA')
            S.append(Bublik(screen))
        return l

class Ball (Bublik):

    def __init__ (self, screen):
        super().__init__(screen)

    def draw_ball (self, screen):
        circle(screen, self.color, (self.x, self.y), self.r)

    def control_ball(self, screen, l):
        if (P[0] - self.x)**2 + (P[1] - self.y)**2 <= self.r**2:
            self.r = 0
            l = l + 1
            print ('U')
            M.append(Ball(screen))
        return l
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False


l = 0 #счетчик очков
p = str(l)
n = 10 #количество шариков

for k in range(n):
    M.append(Ball(screen))


b = 6 #количество бубликов
for i in range(b):
    S.append(Bublik(screen))


f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков: ', True,
                  (180, 180, 0))


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            P = event.pos #координаты мыши

            for ball in M:
                l = ball.control_ball(screen, l)
                ball.control_ball(screen, l)
                p = str(l)
                    
            for bublik in S:
                l = bublik.control_bublik(screen, l)
                bublik.control_bublik(screen, l)
                p = str(l)
        
    
    for bublik in S:
        bublik.draw_bublik(screen)
        bublik.move_bublik(screen)

    for ball in M:
        ball.draw_ball(screen)
        ball.move_bublik(screen)    
    
    screen.blit(text1, (10, 50))
    text2 = f1.render(p, True,
                      (180, 180, 0))
    screen.blit(text2, (300, 50))
    

    pygame.display.update()
    screen.fill(BLACK)

   
print('Поздравляем, ваш счет:', l)

pygame.quit()

dict_rating={}

with open ('results.txt','a') as file:
    file.write(str(name) + ' ' + str(l) + '\n')

with open ('results.txt','r') as file:
    for line_row in file:
        if len(line_row) == 0:
            continue
        line = line_row.strip().split()
        dict_rating.update({line[0]: line[1]})
        dict_rating.items()
        sorted_tuple = sorted(dict_rating.items(), key = lambda x: x[1], reverse = True)
        print (sorted_tuple)
        dict_rating = dict(sorted_tuple)

with open ('results.txt','w') as inf:
        inf.writelines([key+' '+dict_rating[key]+'\n' for key in dict_rating.keys()])


    

    

