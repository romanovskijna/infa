import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))

#голубое небо
sc.fill((0,255,255))

#зеленая трава
rect(sc, (0, 255, 0), (0, 300, 600, 500))

#солнце
circle(sc, (255, 255, 0), (590, 80), 100)
circle(sc, (255, 255, 0), (590, 80), 100, 2)

#единорог
def edinorog (x, y, i, p, k):
    
    #хвост
    ellipse(sc, (255, 143, 193), (x-i*k*53-p*40, y+k*80, k*40,k*9), 0)
    ellipse(sc, (255, 143, 193), (x-i*k*41-p*k*60, y+k*50, k*60,k*9), 0)
    ellipse(sc, (255, 143, 193), (x-i*k*39-p*k*40, y+k*10, k*40,k*30), 0)

    ellipse(sc, (191, 143, 193), (x-i*k*46-p*k*50, y+k*10, k*50,k*20), 0)
    ellipse(sc, (191, 143, 193), (x-i*k*41-p*k*40, y+k*50, k*40,k*9), 0)
    ellipse(sc, (191, 143, 193), (x-i*k*36-p*k*36, y+k*68, k*36,k*16), 0)

    ellipse(sc, (191, 79, 193), (x-i*k*56-p*k*36, y+k*90, k*36,k*26), 0)
    ellipse(sc, (191, 79, 193), (x-i*k*26-p*k*36, y+k*46, k*36,k*14), 0)
    ellipse(sc, (191, 79, 193), (x-i*k*48-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (191, 79, 193), (x-i*k*21-p*k*25, y, k*25,k*13), 0)

    ellipse(sc, (254, 142, 193), (x-i*k*18-p*k*26, y+k*21, k*26,k*20), 0)
    ellipse(sc, (254, 142, 193), (x-i*k*28-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (254, 142, 193), (x-i*k*33-p*k*26, y+k*31, k*26,k*20), 0)
    
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
    ellipse(sc, (191, 79, 193), (x-i*k*62+i*k*140-p*k*40, y+k*80-k*70, k*40,k*9), 0)
    ellipse(sc, (191, 79, 193), (x-i*k*50+i*k*140-p*k*60, y+k*50-k*70, k*60,k*9), 0)
    ellipse(sc, (191, 79, 193), (x-i*k*48+i*k*140-p*k*40, y+k*10-k*70, k*40,k*30), 0)
    
    ellipse(sc, (191, 79, 193), (x-i*k*30+i*k*140-p*k*25, y-k*70, k*25,k*13), 0)

    ellipse(sc, (255, 143, 193), (x-i*k*55+i*k*140-p*k*50, y+k*10-k*70, k*50, k*20), 0)
    ellipse(sc, (255, 143, 193), (x-i*k*50+i*k*140-p*k*40, y+k*50-k*70, k*40, k*9), 0)
    ellipse(sc, (255, 143, 193), (x-i*k*45+k*i*140-p*k*36, y+k*68-k*70, k*36, k*16), 0)

    ellipse(sc, (254, 142, 193), (x-i*k*65+i*k*140-p*k*36, y+k*90-k*70, k*36, k*26), 0)
    ellipse(sc, (254, 142, 193), (x-i*k*35+i*k*140-p*k*36, y+k*46-k*70, k*36, k*14), 0)
    ellipse(sc, (254, 142, 193), (x-i*k*57+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)

    ellipse(sc, (191, 143, 193), (x-i*k*27+i*k*140-p*k*26, y+k*21-k*70, k*26, k*20), 0)
    ellipse(sc, (191, 143, 193), (x-i*k*37+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)
    ellipse(sc, (191, 143, 193), (x-i*k*45+i*k*140-p*k*26, y+k*31-k*70, k*26, k*20), 0)

#дерево
def derevo (x, y, k):
    
    #ствол
    rect(sc, (255, 255, 255), (x, y, 41*k, 120*k), 0)

    #нижний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-k*100, k*160, k*120), 0)

    #средний ярус
    ellipse(sc, (49, 136, 87), (x-k*96, y-k*190, k*240, k*120), 0)

    #верхний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-k*290, k*140, k*180), 0)

    #яблоки
    ellipse(sc, (255, 218, 185), (x+k*50, y-k*25, k*35, k*30), 0)
    ellipse(sc, (255, 218, 185), (x+k*100, y-k*150, k*35, k*30), 0)
    ellipse(sc, (255, 218, 185), (x-k*100, y-k*150, k*35, k*30), 0)
    ellipse(sc, (255, 218, 185), (x+k*25, y-k*245, k*35, k*30), 0)
        
edinorog(280,450,1,0,1.5)
derevo(90, 450, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
