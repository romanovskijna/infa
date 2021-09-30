import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
#голубое небо
screen.fill((0,255,255))
#зеленая трава
rect(screen, (0, 255, 0), (0, 300, 600, 500))
#солнце
circle(screen, (255, 255, 0), (590, 80), 100)
circle(screen, (255, 255, 0), (590, 80), 100, 2)
#единорог


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
