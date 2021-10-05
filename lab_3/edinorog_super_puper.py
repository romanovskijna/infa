import math as m
import pygame
from pygame.draw import *
import random as r
pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))

#голубое небо
sc.fill((0,255,255))

#радуга
A = [(255, 40, 40),(255, 165, 60),(255, 255, 0),(92, 205, 50), (117, 187, 253), (40, 8, 253), (40, 8, 100)]
for i in range (0, 7, 1):
    arc(sc, A[i], (-400-5*i, 0+5*i, 800, 1000), 0, m.pi, 9)

#зеленая трава
rect(sc, (0, 255, 0), (0, 300, 600, 500))

#функция цветочка
def cvetok(k,l,size):
    line(sc, (0, 100, 0), [k,l],[k+2*size,l+3*size])
    line(sc, (0, 100, 0), [k+2*size, l-1*size],[k+2*size,l+3*size])
    ellipse(sc, (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)), (k+1*size, l-8*size , 3*size, 8*size), 0)

#цветочки
for i in range(1,60,1):
    k=r.randint(0,600)
    l=r.randint(300,800)
    size=r.randint(10,30)
    cvetok(k,l,size/10)


#солнце
for i in range(1,200,1):
    ellipse(sc,  (255-2.55/2*i, 255, 2.55/2*i), (500-i, 100-i, 2*i,2*i),2)      


#единорог
def edinorog (x, y, i, p, k, f):
    #хвост
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*53-p*40, y+k*80, k*40,k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*41-p*k*60, y+k*50, k*60,k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*39-p*k*40, y+k*10, k*40,k*30), 0)

    ellipse(sc, (191-f, 143+f, 193), (x-i*k*46-p*k*50, y+k*10, k*50,k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*41-p*k*40, y+k*50, k*40,k*9), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*36-p*k*36, y+k*68, k*36,k*16), 0)

    ellipse(sc, (191-f, 79+f, 193), (x-i*k*56-p*k*36, y+k*90, k*36,k*26), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*26-p*k*36, y+k*46, k*36,k*14), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*48-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*21-p*k*25, y, k*25,k*13), 0)

    ellipse(sc, (254-f, 142+f, 193), (x-i*k*18-p*k*26, y+k*21, k*26,k*20), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*28-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*33-p*k*26, y+k*31, k*26,k*20), 0)
    
    #туловище
    ellipse(sc, (255, 255, 255), (x-i*k*10-p*k*170, y, k*170, k*70), 0)
    
    #ноги
    rect(sc, (255, 255, 255), (x+i*k*10-p*k*3, y+k*30, k*13, k*100))
    rect(sc, (255, 255, 255), (x+i*k*30-p*k*3, y+k*30, k*13, k*110))
    rect(sc, (255, 255, 255), (x+i*k*120-p*k*3, y+k*30, k*13, k*100))
    rect(sc, (255, 255, 255), (x+i*k*140-p*k*3, y+k*30, k*13, k*110))
    
    #шея
    rect(sc, (255, 255, 255), (x+i*k*120-p*k*30, y-k*40, k*30, k*70))
    
    #голова
    ellipse(sc, (255, 255, 255), (x+i*k*112-p*k*50, y-k*65, k*51, k*30), 0)
    ellipse(sc, (255, 255, 255), (x+i*k*142-p*k*36, y-k*55, k*36, k*18), 0)
    
    #глаз
    circle(sc, (241, 79, 193), (x+i*k*149, y-k*55), k*7, 0)
    circle(sc, (0, 0, 0), (x+i*k*151, y-k*53), k*4, 0)
    
    #рог
    polygon(sc, (216, 78, 193), [(x+i*k*135, y-k*65), (x+k*i*135,y-k*115),
                               (x+i*k*143, y-k*65)], 0)
    #грива
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*62+i*k*140-p*k*40, y+k*80-k*70, k*40,k*9), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*50+i*k*140-p*k*60, y+k*50-k*70, k*60,k*9), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*48+i*k*140-p*k*40, y+k*10-k*70, k*40,k*30), 0)
    
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*30+i*k*140-p*k*25, y-k*70, k*25,k*13), 0)

    ellipse(sc, (255-f, 143+f, 193), (x-i*k*55+i*k*140-p*k*50, y+k*10-k*70, k*50, k*20), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*50+i*k*140-p*k*40, y+k*50-k*70, k*40, k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*45+k*i*140-p*k*36, y+k*68-k*70, k*36, k*16), 0)

    ellipse(sc, (254-f, 142+f, 193), (x-i*k*65+i*k*140-p*k*36, y+k*90-k*70, k*36, k*26), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*35+i*k*140-p*k*36, y+k*46-k*70, k*36, k*14), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*57+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)

    ellipse(sc, (191-f, 143+f, 193), (x-i*k*27+i*k*140-p*k*26, y+k*21-k*70, k*26, k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*37+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*45+i*k*140-p*k*26, y+k*31-k*70, k*26, k*20), 0)

#дерево
def derevo (x, y, k, p, spelost):
    
    #ствол
    rect(sc, (255, 255, 255), (x+6*k, y, 35*k, 110*p), 0)
    
    #верхний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-p*290, k*140, p*180), 0)
    ellipse(sc, (0, 255, 0), (x-k*56, y-p*290, k*140, p*180), 2)

    #средний ярус
    ellipse(sc, (49, 136, 87), (x-k*96, y-p*190, k*240, p*120), 0)
    ellipse(sc, (0, 255, 0), (x-k*96, y-p*190, k*240, p*120), 2)

    #нижний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-p*100, k*160, p*120), 0)
    ellipse(sc, (0, 255, 0), (x-k*56, y-p*100, k*160, p*120), 2)
    
    #яблоки
    t=spelost
    ellipse(sc, (255, 218-t, 185-t), (x+k*50, y-p*25, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*50, y-p*25, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*74-k*e, y-p*13-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*74-k*e, y-p*13-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x+k*100, y-p*150, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*100, y-p*150, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*124-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*124-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x-k*90, y-p*150, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x-k*90, y-p*150, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x-k*66-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x-k*66-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x+k*25, y-p*245, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*25, y-p*245, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*49-k*e, y-p*233-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*49-k*e, y-p*233-p*e, 2*p*e, 2*p*e), 2)

edinorog(300,350,1,0,0.6,10)
edinorog(250,570,1,0,1,40)

edinorog(550,450,-1,1,0.8,63)
edinorog(550,300,-1,1, 0.5,35)


derevo(100, 350, 1, 1, 100)
derevo(175, 400, 0.8, 0.5, 70)
derevo(0, 500, 0.9, 0.9, 30)
derevo(133, 590, 0.8, 0.7, 140)
derevo(50, 700, 0.7, 0.7, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
