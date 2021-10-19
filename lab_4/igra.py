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

M = []

def new_ball():
    '''рисует новый шарик '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)

def tozhe_ball(x, y, r, color):
    circle(screen, color, (x, y), r)
    
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

l = 0
p = str(l)
n = 1

for k in range(n):
    new_ball()
    M.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков: ', True,
                  (180, 180, 0))


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            print(event.pos)
            P = event.pos
            for z in range (n):
                if (((M[z - 1][0] - P[0])**2 + (M[z - 1][1] - P[1])**2) < M[z - 1][2]**2):
                    M[z - 1][2] = 0
                    l = l + 1
                    p = str(l)
                    print ('число попаданий: ', l)
                    print ('ura!')
                    
    for i in range (1, n + 1, 1):
        if (M[i - 1][0] < (A - M[i - 1][2]) and  M[i - 1][0] > M[i - 1][2]):
            M[i - 1][0] = M[i - 1][0] + M[i - 1][4]
        else:
            M[i - 1][4] = - M[i - 1][4]
            M[i - 1][0] = M[i - 1][0] + 2 * M[i - 1][4]
            
        if (M[i - 1][1] < (B - M[i - 1][2]) and M[i - 1][1] > M[i - 1][2]):
            M[i - 1][1] = M[i -1 ][1] + M[i - 1][5]
        else:
            M[i - 1][5] = - M[i - 1][5]
            M[i - 1][1] = M[i - 1][1] + 2 * M[i - 1][5] 

                
    screen.blit(text1, (10, 50))
    text2 = f1.render(p, True,
                      (180, 180, 0))
    screen.blit(text2, (300, 50))
    for i in range (n):
        tozhe_ball(M[i - 1][0], M[i - 1][1], M[i - 1][2], M[i - 1][3])
    
    pygame.display.update()
    screen.fill(BLACK)
   
    
   
    
     

pygame.quit()
