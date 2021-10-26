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

def new_bublik():
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r, round(r/4))

def tozhe_bublik(x, y, r, color):
    circle(screen, color, (x, y), r, round(r/4))


def new_ball():
    '''рисует новый шарик '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def tozhe_ball(x, y, r, color):
    circle(screen, color, (x, y), r)
    
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

l = 0 #счетчик очков
p = str(l)
n = 10 #количество шариков

for k in range(n):
    new_ball()
    M.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])

b = 6 #количество бубликов

for i in range(b):
    new_bublik()
    S.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])

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

            for z in range (n):
                if (((M[z - 1][0] - P[0])**2 + (M[z - 1][1] - P[1])**2) < M[z - 1][2]**2):
                    M[z - 1][2] = 0
                    l = l + 1
                    p = str(l)
                    n = n + 1
                    new_ball()
                    M.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])
                    print ('ura!')

            
            for i in range(b): #контролирует попали ли мы в бублики
                if (((S[i - 1][0] - P[0])**2 + (S[i - 1][1] - P[1])**2) < S[i - 1][2]**2) and (((S[i - 1][0] - P[0])**2 + (S[i - 1][1] - P[1])**2) > (S[i - 1][2]*3/4)**2):
                    S[i - 1][2]=0
                    l = l + 2
                    p = str(l)
                    b = b + 1
                    new_bublik()
                    S.append([x, y, r, color, randint(-100, 100) / 20, randint(-100, 100) / 20])
                    print ('ura! ura!')
                    
    for i in range (0, b, 1): #разворот бубликов
        if (S[i][0] < (A - S[i][2]) and  S[i][0] > S[i][2]):
            S[i][0] = S[i][0] + S[i][4]
        else:
            S[i][4] = - S[i][4]
            S[i][0] = S[i][0] + 2 * S[i][4]
            
        if (S[i][1] < (B - S[i][2]) and S[i][1] > S[i][2]):
            S[i][1] = S[i][1] + S[i][5]
        else:
            S[i][5] = - S[i][5]
            S[i][1] = S[i][1] + 2 * S[i][5]

    for i in range (0, n, 1): #разворот шаров
        if (M[i][0] < (A - M[i][2]) and  M[i][0] > M[i][2]):
            M[i][0] = M[i][0] + M[i][4]
        else:
            M[i][4] = - M[i][4]
            M[i][0] = M[i][0] + 2 * M[i][4]
            
        if (M[i][1] < (B - M[i][2]) and M[i][1] > M[i][2]):
            M[i][1] = M[i][1] + M[i][5]
        else:
            M[i][5] = - M[i][5]
            M[i][1] = M[i][1] + 2 * M[i][5] 

                
    screen.blit(text1, (10, 50))
    text2 = f1.render(p, True,
                      (180, 180, 0))
    screen.blit(text2, (300, 50))
    
    for i in range (n):
        tozhe_ball(M[i][0], M[i][1], M[i][2], M[i][3])
    for i in range (b):
        tozhe_bublik(S[i - 1][0], S[i - 1][1], S[i - 1][2], S[i - 1][3])

        
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
        dict_rating = dict(sorted_tuple)
        print(dict_rating)

with open ('results.txt','w') as inf:
        inf.writelines([key+' '+dict_rating[key]+'\n' for key in dict_rating.keys()])


    

    

