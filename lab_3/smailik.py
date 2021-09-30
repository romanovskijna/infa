import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((205,205,205))
#смайлик
circle(screen, (255, 255, 100), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)
#глаз 1
circle(screen, (255, 0, 0), (165, 170), 20)
circle(screen, (0, 0, 0), (165, 170), 20, 2)
circle(screen, (0, 0, 0), (165, 170), 7)
#глаз 2
circle(screen, (255, 0, 0), (235, 170), 15)
circle(screen, (0, 0, 0), (235, 170), 15, 2)
circle(screen, (0, 0, 0), (235, 170), 7)
#брови
polygon(screen, (0, 0, 0), [(190,161), (130,121),
                            (132,119),(192,159),
                            (190,161)], 5)
polygon(screen, (0, 0, 0), [(210,161), (280,120),
                            (282,124),(212,164),
                            (210,161)], 5)
#рот
rect(screen, (0, 0, 0), (150, 250, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
