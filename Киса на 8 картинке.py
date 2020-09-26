import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((660, 1000))

rect (screen, (128, 128, 0), (0, 0, 660, 500)) #стена
rect (screen, (189, 183, 187), (0, 500, 660, 500)) #пол

rect (screen, (0, 255, 255), (360, 40, 270, 420)) #окно

rect (screen, (0, 128, 128), (380, 55, 105, 105)) #верх стёк
rect (screen, (0, 128, 128), (505, 55, 105, 105))
rect (screen, (0, 128, 128), (380, 185, 105, 250)) #ниж стёк
rect (screen, (0, 128, 128), (505, 185, 105, 250))


def xboctn (x, y, r, n):
	for i in range (n - 20):

		circle (screen, (0, 0, 0), (x - 3, y - 1), r - 5, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 5)

xboctn (360, 640, 30, 25)


def xboct (x, y, r, n):
	for i in range (5, n - 5):

		circle (screen, (0, 0, 0), (x + 3 * i, y + i), r, 1)
		circle (screen, (0, 0, 0), (x + 3 * i, y + i), r, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 1)
		circle (screen, (210, 105, 30), (x + 3 * i - 3, y + i - 1), r - 1)		

#		circle (screen, (210, 105, 30), (x + 2 * i + 25, y + i + 25), r - i)
#		circle (screen, (210, 105, 30), (x + i + 30, y + i + 30), r)
#		circle (screen, (210, 105, 30), (x + i + 35, y + i + 35), r/4)

xboct (360, 640, 30, 25)


def xboctk (x, y, r, n):
	for i in range (n - 5, n):

		circle (screen, (0, 0, 0), (x + 73, y + 25), r - 5, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 5)

xboctk (360, 640, 30, 25)


ellipse (screen, (210, 105, 30), (70, 550, 290, 180)) #туловище кисы
ellipse (screen, (0, 0, 0), (70, 550, 290, 180), 1)

ellipse (screen, (210, 105, 30), (50, 640, 50, 80)) #дальняя лапка слева
ellipse (screen, (0, 0, 0), (50, 640, 50, 80), 1)

circle (screen, (210, 104, 30), (70, 640), 55) #голова
circle (screen, (0, 0, 0), (70, 640), 55, 1)

circle (screen, (210, 104, 30), (340, 710), 45) #правая нога
circle (screen, (0, 0, 0), (340, 710), 45, 1)
ellipse (screen, (210, 105, 30), (355, 725, 40, 80)) 
ellipse (screen, (0, 0, 0), (355, 725, 40, 80), 1)

ellipse (screen, (210, 105, 30), (85, 690, 80, 50)) #ближняя лапка слева
ellipse (screen, (0, 0, 0), (85, 690, 80, 50), 1)

circle (screen, (119, 136, 153), (330, 880), 60) #клубок
circle (screen, (0, 0, 0), (330, 880), 60, 1)

arc (screen, (119, 136, 153), (120, 880, 40, 40), 0, 3, 1) #нитка из клубка
arc (screen, (119, 136, 153), (160, 880, 40, 40), 3, 6.28, 1)
arc (screen, (119, 136, 153), (200, 880, 40, 40), 0, 3.14, 1)
arc (screen, (119, 136, 153), (240, 880, 40, 40), 3.14, 6.28, 1)


def nit (x, y, n):
	for i in range (1):
		line (screen, (0, 0, 0), (x, y), (x + n, y + n), 1)
		line (screen, (0, 0, 0), (x + n, y + n), (x + 2 * n, y + 3 * n), 1)
		line (screen, (0, 0, 0), (x + 2 * n, y + 3 * n), (x + 4 * n, y + 4 * n), 1)
		line (screen, (0, 0, 0), (x + 4 * n, y + 4 * n), (x + 5 * n, y + 6 * n), 1)
		line (screen, (0, 0, 0), (x + 5 * n, y + 6 * n), (x + 7 * n, y + 7 * n), 1)
		line (screen, (0, 0, 0), (x + 7 * n, y + 7 * n), (x + 8 * n, y + 9 * n), 1)
		line (screen, (0, 0, 0), (x + 8 * n, y + 9 * n), (x + 10 * n, y + 10 * n), 1)
		line (screen, (0, 0, 0), (x + 10 * n, y + 10 * n), (x + 11 * n, y + 12 * n), 1)

nit (300, 850, 5)

nit (310, 845, 5)

nit (320, 842, 5)

nit (330, 840, 5)


def nitN (x, y, n):
	for i in range (1):
		line (screen, (0, 0, 0), (x, y), (x - n, y + n), 1)
		line (screen, (0, 0, 0), (x - n, y + n), (x - 2 * n, y + 3 * n), 1)
		line (screen, (0, 0, 0), (x - 2 * n, y + 3 * n), (x - 4 * n, y + 4 * n), 1)
		line (screen, (0, 0, 0), (x - 4 * n, y + 4 * n), (x - 5 * n, y + 6 * n), 1)

nitN (300, 860, 3)

nitN (303, 880, 3)

nitN (317, 900, 4)



#lines (screen, (119, 136, 153), 1, (325, 830), (327, 850), (330, 880), (333, 810), (335, 930), 1) #нитка v клубкe


circle (screen, (0, 128, 0), (50, 620), 15) #глаза
circle (screen, (0, 0, 0), (50, 620), 15, 1)
circle (screen, (0, 128, 0), (90, 620), 15) 
circle (screen, (0, 0, 0), (90, 620), 15, 1)
ellipse (screen, (0, 0, 0), (85, 607, 10, 26)) #зрачки
ellipse (screen, (0, 0, 0), (45, 607, 10, 26)) 


def zrach1 (x, y, r, n):
	for i in range (n - 6):
		circle (screen, (255, 255, 255), (x + i, y + i), r - 2)

zrach1 (44, 614, 3, 8)
zrach1 (84, 614, 3, 8)

def zrach2 (x, y, r, n):
	for i in range (n - 6, n - 2):
		circle (screen, (255, 255, 255), (x + i, y + i), r)

zrach2 (44, 614, 3, 8)
zrach2 (84, 614, 3, 8)


def zrach3 (x, y, r, n):
	for i in range (n - 2, n):
		circle (screen, (255, 255, 255), (x + i, y + i), r - 2)

zrach3 (44, 614, 3, 8)
zrach3 (84, 614, 3, 8)


polygon (screen, (245, 222, 179), ((70, 643), (67, 637), (73, 637))) #нос
polygon (screen, (0, 0, 0), ((70, 643), (67, 637), (73, 637)), 1)

polygon (screen, (210, 105, 30), ((42, 572), (44, 595), (57, 587))) #ухо Л
polygon (screen, (0, 0, 0), ((42, 572), (44, 595), (57, 585)), 1)
polygon (screen, (222, 184, 135), ((45, 575), (47, 592), (54, 587))) #внут
polygon (screen, (0, 0, 0), ((45, 575), (47, 592), (54, 587)), 1)

polygon (screen, (210, 105, 30), ((98, 572), (96, 595), (83, 587))) #ухо П
polygon (screen, (0, 0, 0), ((98, 572), (96, 595), (83, 585)), 1)
polygon (screen, (222, 184, 135), ((95, 575), (93, 592), (86, 587))) #внут
polygon (screen, (0, 0, 0), ((95, 575), (93, 592), (86, 587)), 1)

line (screen, (0, 0, 0), (70, 643), (70, 660), 1) #рот
arc (screen, (0, 0, 0), (70, 650, 15, 15), 10, 6, 1)
arc (screen, (0, 0, 0), (55, 650, 15, 15), 10, 6, 1)

arc (screen, (105, 105, 105), (73, 640, 73, 30), 1, 3, 1) #усы
arc (screen, (105, 105, 105), (73, 646, 73, 30), 1, 3, 1)
arc (screen, (105, 105, 105), (73, 652, 73, 30), 1, 3, 1)
arc (screen, (105, 105, 105), (0, 640, 73, 30), 0.5, 2.5, 1)
arc (screen, (105, 105, 105), (0, 646, 73, 30), 0.5, 2.5, 1)
arc (screen, (105, 105, 105), (0, 652, 73, 30), 0.5, 2.5, 1)





#def xboct (x1, y1, N):
#	x1_size = N * 125
#	y1_size = N * 100
#	arc (screen, (222, 184, 135), pugame.rect(x1, y1, x1_size, y1_size), np.pi / 2, np.pi, N)
#	for i in range (1, N + 1):
#		eellipse (screen, color_green, (x1 + 0.35 * x1_size * i , y1 - 0.2 * y1_size * i , N * 5, N * 25))
#
#
#xboct (100, 200, 10)




#for step in range (1):
#
#	x = 340
#	while x < 480:
#		x += 1
#		for n in range (1):
#			polygon (screen, (210, 105, 30), ((x, 260+x)), 0)
#
#
#ellipse (screen, (210, 105, 30), ((340, 600), (420, 620), (480, 680), (400, 660)), 0) хвост
 

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()