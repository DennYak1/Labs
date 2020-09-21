import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect (screen, (255, 255, 255), (0, 0, 400, 400))

circle (screen, (255, 255, 0), (200, 175), 150)
circle (screen, (0, 0, 0), (200, 175), 150, 5)

rect (screen, (0, 0, 0), (160, 280, 80, 20))

circle (screen, (255, 0, 0), (125, 100), 35)
circle (screen, (255, 0, 0), (275, 100), 35)
circle (screen, (0, 0, 0), (125, 100), 15)
circle (screen, (0, 0, 0), (275, 100), 15)

polygon (screen, (0, 0, 0), [[100, 50], [90, 40], [210, 110], [220, 120]])
polygon (screen, (0, 0, 0), [[300, 50], [310, 40], [190, 110], [180, 120]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()