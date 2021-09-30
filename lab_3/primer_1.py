import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((155,155,155))

circle(screen, (255, 255, 100), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)

circle(screen, (255, 0, 0), (169, 150), 20)
circle(screen, (0, 0, 0), (169, 150), 20, 2)
circle(screen, (0, 0, 0), (169, 150), 5)

circle(screen, (255, 0, 0), (240, 150), 15)
circle(screen, (0, 0, 0), (240, 150), 15, 2)
circle(screen, (0, 0, 0), (240, 150), 5)

polygon(screen, (0, 0, 0), [(150,105), (200,150),
                            (201,149),(145,103),
                            (150,105)], 5)
polygon(screen, (0, 0, 0), [(250,105), (200,150),
                            (201,149),(250,103),
                            (250,105)], 5)
#брови

rect(screen, (0, 0, 0), (150, 220, 100, 15))#рот

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
