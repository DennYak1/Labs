import pygame
import numpy as np

from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((1200, 800))

color_green = (0, 255, 0)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_toxic = (230, 0, 255, 255)


def vetka_vpravo(x1, y1, size1, num_list): #рисует ветку вправо
    x1_size = size1 * 125
    y1_size = size1 * 100
    arc(screen, color_green, pygame.Rect(x1, y1, x1_size, y1_size),
        np.pi / 2, np.pi, size1)
    for i in range(1, num_list+1):
        ellipse(screen, color_green, (x1 + 0.35 * x1_size * i / num_list,
                y1 - 0.2 * y1_size * i / num_list, size1 * 5, size1 * 25))


def vetka_vgolovu(x, y, size, num_list): #рисует ветку влево
    x_size = size * 125
    y_size = size * 100
    arc(screen, color_green, pygame.Rect(x - x_size, y,
        x_size, y_size), 0, np.pi / 2, size)
    for i in range(1, num_list+1):
        ellipse(screen, color_green, (x - 0.35 * x_size * i / num_list,
                y - 0.2 * y_size * i / num_list, size * 5, size * 25))


def bambuk(x, y, size, splush): #рисует бамбук
    x_size = size*10*splush
    y_size = size*30
    rect(screen, color_green, (x, y, x_size, y_size))
    rect(screen, color_green, (x, y - 1.1 * y_size, x_size, y_size))
    polygon(screen, color_green, [(x + size * 4, y - 2.3 * y_size),
            (x + x_size, y - 2.2 * y_size), (x + size * 4, y - 1.3 * y_size),
            (x - size * 2, y - 1.4 * y_size)])
    polygon(screen, color_green, [(x + size * 6, y - 2.5 * y_size),
            (x + size * 10, y - 2.4 * y_size),
            (x + size * 12, y - 3.1 * y_size),
            (x + size * 8, y - 3.2 * y_size)])

    vetka_vpravo(x + x_size * 1.4, y - y_size * 2.8, 3, 4)
    vetka_vpravo(x + x_size * 1.2, y - y_size * 2.1, 2, 3)
    vetka_vpravo(x + x_size * 1.05, y - y_size * 1.7, 2, 2)

    vetka_vgolovu(x - x_size * 0.6, y - y_size * 2.8, 3, 4)
    vetka_vgolovu(x - x_size * 0.4, y - y_size * 2.1, 2, 3)
    vetka_vgolovu(x - x_size * 0.3, y - y_size * 1.7, 2, 2)

def Reversed(x, y, size, color, q, o): #рисует перевёрнутого медведя
    x_size = size * 50
    y_size = size * 30
    x = x + x_size
    ellipse(screen, color_black, (x, y, x_size, y_size))

    ellipse(screen, color, (x - x_size * 4.3 * o,
            y + y_size * 2 / 3, x_size * 5, y_size * 5))

    rect(screen, color_black, (x - x_size * 1.8 * q,
         y + y_size * 8 / 3, x_size * 6 / 5, y_size * 10 / 3))
    ellipse(screen, color_black, (x - x_size * 2 * q,
            y + y_size * 11 / 3, x_size, y_size * 10 / 3))
    ellipse(screen, color_black, (x - x_size * 1.7 * q,
            y + y_size * 17 / 3, x_size * 1.6, y_size * 5 / 3))
    ellipse(screen, color_black, (x - x_size * 4 * q,
            y + y_size * 11 / 3, x_size, y_size * 10 / 3))
    ellipse(screen, color_black, (x - x_size * 3.7 * q,
            y + y_size * 17 / 3, x_size * 1.6, y_size * 5 / 3))
    ellipse(screen, color_black, (x - x_size * 0.2 * q,
            y + y_size * 10 / 3, x_size, y_size * 10 / 3))

    ellipse(screen, color, (x - x_size * 1.8 * o,
            y - y_size / 3, x_size * 3, y_size * 6))

    ellipse(screen, color_black, (x + x_size * 0.2 * q,
            y + y_size * 4 / 3, x_size * 4 / 5, y_size * 5 / 3))
    ellipse(screen, color_black, (x - x_size * q,
            y + y_size * 4 / 3, x_size, y_size * 5 / 3))
    ellipse(screen, color_black, (x - x_size * 0.1 * 0,
            y + y_size * 4, 40, y_size))
    ellipse(screen, color_black, (x - x_size * 1.8 * q,
            y, x_size, y_size))

rect(screen, (255, 94, 196), (0, 0, 1200, 800))

Reversed(600, 280, 0.8, color_toxic, -1, 0)

Reversed(300, 280, 0.8, color_toxic, 1, 1)

bambuk(485, 400, 4, 0.6)
bambuk(900, 350, 3, 1)
bambuk(50, 300, 3, 1)
bambuk(200, 650, 3, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
