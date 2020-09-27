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

rect (screen, (0, 255, 255), (360 - 300, 40, 270, 420)) #окно

rect (screen, (0, 128, 128), (380 - 300, 55, 105, 105)) #верх стёк
rect (screen, (0, 128, 128), (505 - 300, 55, 105, 105))
rect (screen, (0, 128, 128), (380 - 300, 185, 105, 250)) #ниж стёк
rect (screen, (0, 128, 128), (505 - 300, 185, 105, 250))

rect (screen, (0, 255, 255), (360 - 600, 40, 270, 420)) #окно

rect (screen, (0, 128, 128), (380 - 600, 55, 105, 105)) #верх стёк
rect (screen, (0, 128, 128), (505 - 600, 55, 105, 105))
rect (screen, (0, 128, 128), (380 - 600, 185, 105, 250)) #ниж стёк
rect (screen, (0, 128, 128), (505 - 600, 185, 105, 250))


circle (screen, (119, 136, 153), (130, 580), 15) #клубок1
circle (screen, (0, 0, 0), (130, 580), 15, 1)

circle (screen, (119, 136, 153), (390, 700), 30) #клубок2
circle (screen, (0, 0, 0), (390, 700), 30, 1)

circle (screen, (119, 136, 153), (500, 650), 10) #клубок3
circle (screen, (0, 0, 0), (500, 650), 10, 1)

circle (screen, (119, 136, 153), (80, 880), 12) #клубок4
circle (screen, (0, 0, 0), (80, 880), 12, 1)

circle (screen, (119, 136, 153), (300, 880), 60) #клубок5
circle (screen, (0, 0, 0), (300, 880), 60, 1)

circle (screen, (119, 136, 153), (550, 880), 20) #клубок6
circle (screen, (0, 0, 0), (550, 880), 20, 1)

circle (screen, (119, 136, 153), (510, 950), 7) #клубок7
circle (screen, (0, 0, 0), (510, 950), 7, 1)


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

nit (121, 573, 1) #1
nit (128, 570, 1)

nit (372, 685, 2) #2
nit (387, 690, 2)
nit (395, 684, 2)
nit (398, 678, 2)

nit (495, 643, 1) #3
#nit (498, 640, 1)

nit (74, 874, 1) #4
#nit (78, 870, 1)

nit (267, 850, 5) #5
nit (282, 855, 5)
nit (290, 849, 5)
nit (293, 843, 5)

nit (536, 869, 2) #6
nit (544, 870, 2)
nit (548, 866, 2)

#nit (501, 943, 1) #7
#nit (508, 940, 1)

def nitN (x, y, n):
	for i in range (1):
		line (screen, (0, 0, 0), (x, y), (x - n, y + n), 1)
		line (screen, (0, 0, 0), (x - n, y + n), (x - 2 * n, y + 3 * n), 1)
		line (screen, (0, 0, 0), (x - 2 * n, y + 3 * n), (x - 4 * n, y + 4 * n), 1)
		line (screen, (0, 0, 0), (x - 4 * n, y + 4 * n), (x - 5 * n, y + 6 * n), 1)

nitN (378, 700, 2) #2

nitN (280, 880, 3) #5
nitN (282, 890, 3)

nitN (547, 882, 2) #6


arc (screen, (119, 136, 153), (75, 580, 10, 10), 0, 3, 1) #нитка из клубка1
arc (screen, (119, 136, 153), (85, 580, 10, 10), 3, 6.28, 1)
arc (screen, (119, 136, 153), (95, 580, 10, 10), 0, 3.14, 1)
arc (screen, (119, 136, 153), (105, 580, 10, 10), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (290, 700, 20, 20), 0, 3, 1) #нитка из клубка2
arc (screen, (119, 136, 153), (310, 700, 20, 20), 3, 6.28, 1)
arc (screen, (119, 136, 153), (330, 700, 20, 20), 0, 3.14, 1)
arc (screen, (119, 136, 153), (350, 700, 20, 20), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (472, 650, 7, 7), 0, 3, 1) #нитка из клубка3
arc (screen, (119, 136, 153), (479, 650, 7, 7), 3, 6.28, 1)
arc (screen, (119, 136, 153), (486, 650, 7, 7), 0, 3.14, 1)
arc (screen, (119, 136, 153), (493, 650, 7, 7), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (46, 880, 8, 8), 0, 3, 1) #нитка из клубка4
arc (screen, (119, 136, 153), (54, 880, 8, 8), 3, 6.28, 1)
arc (screen, (119, 136, 153), (62, 880, 8, 8), 0, 3.14, 1)
arc (screen, (119, 136, 153), (70, 880, 8, 8), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (90, 880, 40, 40), 0, 3, 1) #нитка из клубка5
arc (screen, (119, 136, 153), (130, 880, 40, 40), 3, 6.28, 1)
arc (screen, (119, 136, 153), (170, 880, 40, 40), 0, 3.14, 1)
arc (screen, (119, 136, 153), (210, 880, 40, 40), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (488, 880, 13, 13), 0, 3, 1) #нитка из клубка6
arc (screen, (119, 136, 153), (501, 880, 13, 13), 3, 6.28, 1)
arc (screen, (119, 136, 153), (514, 880, 13, 13), 0, 3.14, 1)
arc (screen, (119, 136, 153), (527, 880, 13, 13), 3.14, 6.28, 1)

arc (screen, (119, 136, 153), (493, 950, 4, 4), 0, 3, 1) #нитка из клубка7
arc (screen, (119, 136, 153), (497, 950, 4, 4), 3, 6.28, 1)
arc (screen, (119, 136, 153), (501, 950, 4, 4), 0, 3.14, 1)
arc (screen, (119, 136, 153), (505, 950, 4, 4), 3.14, 6.28, 1)


#РЫЖИЕ ВЛЕВО
def xboctn (x, y, r, n, L):
	for i in range (n - L):
		circle (screen, (0, 0, 0), (x - 3, y - 1), r - 2, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 2)

xboctn (140, 480, 12, 15, 12)
xboctn (600, 920, 8, 12, 10)

def xboct (x, y, r, n, L):
	for i in range (n - L, L ):
		circle (screen, (0, 0, 0), (x + 3 * i + 1, y + i), r, 1)
		circle (screen, (0, 0, 0), (x + 3 * i - 1, y + i), r, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 1)
		circle (screen, (210, 105, 30), (x + 3 * i - 3, y + i - 1), r - 1)
		
xboct (140, 480, 12, 15, 12)
xboct (600, 920, 8, 12, 10)

def xboctk (x, y, r, n, L):
	for i in range (L, n):
		circle (screen, (0, 0, 0), (x + 3 * i, y + i), r - 2, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y + i), r - 2)

xboctk (140, 480, 12, 15, 12)
xboctk (600, 920, 8, 12, 10)

#ЧЁРНЫЕ ВЛЕВО
def xboctn (x, y, r, n, L):
	for i in range (n - L):
		circle (screen, (0, 0, 0), (x - 3, y - 1), r - 2, 1)
		circle (screen, (105, 105, 105), (x + 3 * i, y + i), r - 2)

xboctn (590, 572, 20, 30, 24)

def xboct (x, y, r, n, L):
	for i in range (n - L, L ):
		circle (screen, (0, 0, 0), (x + 3 * i + 1, y + i), r, 1)
		circle (screen, (0, 0, 0), (x + 3 * i - 1, y + i), r, 1)
		circle (screen, (105, 105, 105), (x + 3 * i, y + i), r - 1)
		circle (screen, (105, 105, 105), (x + 3 * i - 3, y + i - 1), r - 1)
xboct (590, 572, 20, 30, 24)

def xboctk (x, y, r, n, L):
	for i in range (L, n):
		circle (screen, (0, 0, 0), (x + 3 * i, y + i), r - 2, 1)
		circle (screen, (105, 105, 105), (x + 3 * i, y + i), r - 2)

xboctk (590, 572, 20, 30, 24)

#РЫЖИЕ ВПРАВО
def xboctk (x, y, r, n, L):
	for i in range (L, n):
		circle (screen, (0, 0, 0), (x - 3 * i - 1, y + i + 1), r - 5, 1)
		circle (screen, (210, 105, 30), (x - 3 * i, y + i), r - 5)
		circle (screen, (210, 105, 30), (x - 3 * i, y + i), r - 5)

xboctk (60, 760, 20, 15, 10)
xboctk (60, 650, 15, 12, 8)

def xboct (x, y, r, n, L):
	for i in range (n - L, L ):
		circle (screen, (0, 0, 0), (x - 3 * i + 1, y + i), r, 1)
		circle (screen, (0, 0, 0), (x - 3 * i - 1, y + i), r, 1)
		circle (screen, (210, 105, 30), (x - 3 * i, y + i), r - 1)
		circle (screen, (210, 105, 30), (x - 3 * i - 3, y + i + 1), r - 1)
		circle (screen, (210, 105, 30), (x - 3 * i, y + i + 1), r - 1)

xboct (60, 760, 20, 15, 10)
xboct (60, 650, 15, 12, 8)

def xboctn (x, y, r, n, L):
	for i in range (n - L):
		circle (screen, (0, 0, 0), (x + 3 * i + 1, y - i - 1), r - 5, 1)
		circle (screen, (210, 105, 30), (x + 3 * i, y - i), r - 5)
		circle (screen, (210, 105, 30), (x - 3 * i, y + i), r - 5)

xboctn (60, 760, 20, 15, 10)
xboctn (60, 650, 15, 12, 8)



#KisaBR (410, 720, 200, 100, 25, 420, 670, 6)

#KisaBR (110, 900, 140, 70, 20, 120, 860, 4)


#ЧЁРНЫЕ ВПРАВО
def xboctk (x, y, r, n, L):
	for i in range (L, n):
		circle (screen, (0, 0, 0), (x - 3 * i - 1, y + i + 1), r - 5, 1)
		circle (screen, (105, 105, 105), (x - 3 * i, y + i), r - 5)
		circle (screen, (105, 105, 105), (x - 3 * i, y + i), r - 5)

xboctk (410, 770, 20, 20, 15)
xboctk (110, 940, 15, 15, 10)

def xboct (x, y, r, n, L):
	for i in range (n - L, L ):
		circle (screen, (0, 0, 0), (x - 3 * i + 1, y + i), r, 1)
		circle (screen, (0, 0, 0), (x - 3 * i - 1, y + i), r, 1)
		circle (screen, (105, 105, 105), (x - 3 * i, y + i), r - 1)
		circle (screen, (105, 105, 105), (x - 3 * i - 3, y + i + 1), r - 1)
		circle (screen, (105, 105, 105), (x - 3 * i, y + i + 1), r - 1)

xboct (410, 770, 20, 20, 15)
xboct (110, 940, 15, 15, 10)

def xboctn (x, y, r, n, L):
	for i in range (n):
		circle (screen, (0, 0, 0), (x + 3 * i + 1, y - i - 1), r - 5, 1)
		circle (screen, (105, 105, 105), (x + 3 * i, y - i), r - 5)
		circle (screen, (105, 105, 105), (x - 3 * i, y + i), r - 5)

xboctn (410, 770, 20, 20, 15)
xboctn (110, 940, 15, 15, 10)


#кошка смотрящая вЛЕВО
def KisaOL (x, y, x1, y1, r, xe, ye, re):
	ellipse (screen, (210, 105, 30), (x, y, x1, y1)) #туловище кисы
	ellipse (screen, (0, 0, 0), (x, y, x1, y1), 1)

	ellipse (screen, (210, 105, 30), (x  - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2)) #дальняя лапка слева
	ellipse (screen, (0, 0, 0), (x  - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2), 1)

	circle (screen, (210, 105, 30), (x, y + 2 * r), r) #голова
	circle (screen, (0, 0, 0), (x , y + 2 * r), r, 1)

	circle (screen, (210, 105, 30), (x + x1 - r, y + y1 - r), r - 2) #правая нога
	circle (screen, (0, 0, 0), (x + x1 - r, y + y1 - r), r - 2, 1)

	ellipse (screen, (210, 105, 30), (x + x1 - 4 * r / 5, y + y1 - 4 * r / 5, r, 2 * r)) 
	ellipse (screen, (0, 0, 0), (x + x1 - 4 * r / 5, y + y1 - 4 * r / 5, r, 2 * r), 1)

	ellipse (screen, (210, 105, 30), (x, y + y1 - 3 * r / 5, x1 / 2, y1 / 5)) #ближняя лапка слева
	ellipse (screen, (0, 0, 0), (x, y + y1 - 3 * r / 5, x1 / 2, y1 / 5), 1)

	circle (screen, (0, 128, 0), (xe, ye), re) #глаза
	circle (screen, (0, 0, 0), (xe, ye), re, 1)
	circle (screen, (0, 128, 0), (2 * x - xe, ye), re) 
	circle (screen, (0, 0, 0), (2 * x - xe, ye), re, 1)

	ellipse (screen, (0, 0, 0), (xe, ye - re, re, 2 * re)) #зрачки
	ellipse (screen, (0, 0, 0), (2 * x - xe, ye- re, re, 2 * re)) 

	polygon (screen, (245, 222, 179), ((x, y + re + 2 * r), (x - re, y - re + 2 * r), (x + re, y - re + 2 * r))) #нос
	polygon (screen, (0, 0, 0), ((x, y + re + 2 * r), (x - re, y - re + 2 * r), (x + re, y - re + 2 * r)), 1)

	polygon (screen, (210, 105, 30), ((x - r, y + r), (x - r + re, y + 3 * re + r), (x - r + 2 * re, y + 2 * re + r))) #ухо Л
	polygon (screen, (0, 0, 0), ((x - r, y + r), (x - r + re, y + 3 * re + r), (x - r + 2 * re, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x - r + 1, y + r + 1), (x - r + re - 1, y + 3 * re + r - 1), (x - r + 2 * re - 1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x - r + 1, y + r + 1), (x - r + re , y + 3 * re + r - 1), (x - r + 2 * re - 1, y + 2 * re + r)), 1)

	polygon (screen, (210, 105, 30), ((x + r, y + r), (x + r - re, y + 3 * re + r), (x + r - 2 * re, y + 2 * re + r))) #ухо П
	polygon (screen, (0, 0, 0), ((x + r, y + r), (x + r - re, y + 3 * re + r), (x + r - 2 * re, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x + r - 1, y + r + 1), (x + r - re, y + 3 * re + r - 1), (x + r - 2 * re + 1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x + r - 1, y + r + 1), (x + r - re, y + 3 * re + r - 1), (x + r - 2 * re + 1, y + 2 * re + r)), 1)

	line (screen, (0, 0, 0), (x, y + re + 2 * r), (x, y + 2 * re + 2 * r), 1) #рот
	arc (screen, (0, 0, 0), (x, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)
	arc (screen, (0, 0, 0), (x - 2 * re, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)

	arc (screen, (105, 105, 105), (x, y + 2 * r, r, 3 * re), 1, 3, 1) #усы
	arc (screen, (105, 105, 105), (x, y + 2 * r + re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x, y + 2 * r + 2 * re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r + re, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r + 2 * re, r, 3 * re), 0.5, 2.5, 1)

def KisaBL (x, y, x1, y1, r, xe, ye, re):
	ellipse (screen, (105, 105, 105), (x, y, x1, y1)) #туловище кисы
	ellipse (screen, (0, 0, 0), (x, y, x1, y1), 1)

	ellipse (screen, (105, 105, 105), (x  - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2)) #дальняя лапка слева
	ellipse (screen, (0, 0, 0), (x  - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2), 1)

	circle (screen, (105, 105, 105), (x, y + 2 * r), r) #голова
	circle (screen, (0, 0, 0), (x , y + 2 * r), r, 1)

	circle (screen, (105, 105, 105), (x + x1 - r, y + y1 - r), r - 2) #правая нога
	circle (screen, (0, 0, 0), (x + x1 - r, y + y1 - r), r - 2, 1)

	ellipse (screen, (105, 105, 105), (x + x1 - 4 * r / 5, y + y1 - 4 * r / 5, r, 2 * r)) 
	ellipse (screen, (0, 0, 0), (x + x1 - 4 * r / 5, y + y1 - 4 * r / 5, r, 2 * r), 1)

	ellipse (screen, (105, 105, 105), (x, y + y1 - 3 * r / 5, x1 / 2, y1 / 5)) #ближняя лапка слева
	ellipse (screen, (0, 0, 0), (x, y + y1 - 3 * r / 5, x1 / 2, y1 / 5), 1)

	circle (screen, (0, 255, 255), (xe, ye), re) #глаза
	circle (screen, (0, 0, 0), (xe, ye), re, 1)
	circle (screen, (0, 255, 255), (2 * x - xe, ye), re) 
	circle (screen, (0, 0, 0), (2 * x - xe, ye), re, 1)

	ellipse (screen, (0, 0, 0), (xe - re / 2, ye - re, re, 2 * re)) #зрачки
	ellipse (screen, (0, 0, 0), (2 * x - xe - re / 2, ye - re, re, 2 * re)) 

	polygon (screen, (245, 222, 179), ((x, y + re + 2 * r), (x - re, y - re + 2 * r), (x + re, y - re + 2 * r))) #нос
	polygon (screen, (0, 0, 0), ((x, y + re + 2 * r), (x - re, y - re + 2 * r), (x + re, y - re + 2 * r)), 1)

	polygon (screen, (210, 105, 30), ((x - r, y + r), (x - r + re, y + 3 * re + r), (x - r + 2 * re, y + 2 * re + r))) #ухо Л
	polygon (screen, (0, 0, 0), ((x - r, y + r), (x - r + re, y + 3 * re + r), (x - r + 2 * re, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x - r + 1, y + r + 1), (x - r + re - 1, y + 3 * re + r - 1), (x - r + 2 * re - 1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x - r + 1, y + r + 1), (x - r + re , y + 3 * re + r - 1), (x - r + 2 * re - 1, y + 2 * re + r)), 1)

	polygon (screen, (210, 105, 30), ((x + r, y + r), (x + r - re, y + 3 * re + r), (x + r - 2 * re, y + 2 * re + r))) #ухо П
	polygon (screen, (0, 0, 0), ((x + r, y + r), (x + r - re, y + 3 * re + r), (x + r - 2 * re, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x + r - 1, y + r + 1), (x + r - re, y + 3 * re + r - 1), (x + r - 2 * re + 1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x + r - 1, y + r + 1), (x + r - re, y + 3 * re + r - 1), (x + r - 2 * re + 1, y + 2 * re + r)), 1)

	line (screen, (0, 0, 0), (x, y + re + 2 * r), (x, y + 2 * re + 2 * r), 1) #рот
	arc (screen, (0, 0, 0), (x, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)
	arc (screen, (0, 0, 0), (x - 2 * re, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)

	arc (screen, (105, 105, 105), (x, y + 2 * r, r, 3 * re), 1, 3, 1) #усы
	arc (screen, (105, 105, 105), (x, y + 2 * r + re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x, y + 2 * r + 2 * re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r + re, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r, y + 2 * r + 2 * re, r, 3 * re), 0.5, 2.5, 1)

#кошка смотрящая вПРАВО
def KisaOR (x, y, x1, y1, r, xe, ye, re):
	ellipse (screen, (210, 105, 30), (x, y, x1, y1)) #туловище кисы
	ellipse (screen, (0, 0, 0), (x, y, x1, y1), 1)

	ellipse (screen, (210, 105, 30), (x + x1 - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2)) #дальняя лапка слева
	ellipse (screen, (0, 0, 0), (x + x1 - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2), 1)

	circle (screen, (210, 105, 30), (x + x1, y + 2 * r), r) #голова
	circle (screen, (0, 0, 0), (x + x1, y + 2 * r), r, 1)

	circle (screen, (210, 105, 30), (x + r - re, y + y1 - r), r - 2) #правая нога
	circle (screen, (0, 0, 0), (x + r - re, y + y1 - r), r - 2, 1)

	ellipse (screen, (210, 105, 30), (x - re, y + y1 - 4 * r / 5, r, 2 * r)) 
	ellipse (screen, (0, 0, 0), (x - re, y + y1 - 4 * r / 5, r, 2 * r), 1)

	ellipse (screen, (210, 105, 30), (x + x1 / 2, y + y1 - 3 * r / 5, x1 / 2, y1 / 5)) #ближняя лапка слева
	ellipse (screen, (0, 0, 0), (x + x1 / 2, y + y1 - 3 * r / 5, x1 / 2, y1 / 5), 1)

	circle (screen, (0, 128, 0), (xe + x1, ye + 4 * r - 2 * re), re) #глаза
	circle (screen, (0, 0, 0), (xe + x1, ye + 4 * r - 2 * re), re, 1)
	circle (screen, (0, 128, 0), (2 * x - xe + x1, ye + 4 * r - 2 * re), re) 
	circle (screen, (0, 0, 0), (2 * x - xe + x1, ye + 4 * r - 2 * re), re, 1)

	ellipse (screen, (0, 0, 0), (xe + x1 - re / 2, ye + 4 * r - 3 * re, re, 2 * re)) #зрачки
	ellipse (screen, (0, 0, 0), (2 * x - xe + x1 - re / 2, ye + 4 * r - 3 * re, re, 2 * re))

	polygon (screen, (245, 222, 179), ((x + x1, y + re + 2 * r), (x - re + x1, y - re + 2 * r), (x + re + x1, y - re + 2 * r))) #нос
	polygon (screen, (0, 0, 0), ((x + x1, y + re + 2 * r), (x - re + x1, y - re + 2 * r), (x + re + x1, y - re + 2 * r)), 1)

	polygon (screen, (210, 105, 30), ((x - r + x1, y + r), (x - r + re + x1, y + 3 * re + r), (x - r + 2 * re + x1, y + 2 * re + r))) #ухо Л
	polygon (screen, (0, 0, 0), ((x - r + x1, y + r), (x - r + re + x1, y + 3 * re + r), (x - r + 2 * re + x1, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x - r + 1 + x1, y + r + 1), (x - r + re - 1 + x1, y + 3 * re + r - 1), (x - r + 2 * re - 1 + x1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x - r + 1 + x1, y + r + 1), (x - r + re + x1, y + 3 * re + r - 1), (x - r + 2 * re - 1 + x1, y + 2 * re + r)), 1)

	polygon (screen, (210, 105, 30), ((x + r + x1, y + r), (x + r - re + x1, y + 3 * re + r), (x + r - 2 * re + x1, y + 2 * re + r))) #ухо П
	polygon (screen, (0, 0, 0), ((x + r + x1, y + r), (x + r - re + x1, y + 3 * re + r), (x + r - 2 * re + x1, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x + r - 1 + x1, y + r + 1), (x + r - re + x1, y + 3 * re + r - 1), (x + r - 2 * re + 1 + x1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x + r - 1 + x1, y + r + 1), (x + r - re + x1, y + 3 * re + r - 1), (x + r - 2 * re + 1 + x1, y + 2 * re + r)), 1)

	line (screen, (0, 0, 0), (x + x1, y + re + 2 * r), (x + x1, y + 2 * re + 2 * r), 1) #рот
	arc (screen, (0, 0, 0), (x + x1, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)
	arc (screen, (0, 0, 0), (x - 2 * re + x1, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)

	arc (screen, (105, 105, 105), (x + x1, y + 2 * r, r, 3 * re), 1, 3, 1) #усы
	arc (screen, (105, 105, 105), (x + x1, y + 2 * r + re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x + x1, y + 2 * r + 2 * re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r + re, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r + 2 * re, r, 3 * re), 0.5, 2.5, 1)

def KisaBR (x, y, x1, y1, r, xe, ye, re):
	ellipse (screen, (105, 105, 105), (x, y, x1, y1)) #туловище кисы
	ellipse (screen, (0, 0, 0), (x, y, x1, y1), 1)

	ellipse (screen, (105, 105, 105), (x + x1 - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2)) #дальняя лапка слева
	ellipse (screen, (0, 0, 0), (x + x1 - 3 * r / 5, y + y1 / 2, x1 / 5, y1 / 2), 1)

	circle (screen, (105, 105, 105), (x + x1, y + 2 * r), r) #голова
	circle (screen, (0, 0, 0), (x + x1, y + 2 * r), r, 1)

	circle (screen, (105, 105, 105), (x + r - re, y + y1 - r), r - 2) #правая нога
	circle (screen, (0, 0, 0), (x + r - re, y + y1 - r), r - 2, 1)

	ellipse (screen, (105, 105, 105), (x - re, y + y1 - 4 * r / 5, r, 2 * r)) 
	ellipse (screen, (0, 0, 0), (x - re, y + y1 - 4 * r / 5, r, 2 * r), 1)

	ellipse (screen, (105, 105, 105), (x + x1 / 2, y + y1 - 3 * r / 5, x1 / 2, y1 / 5)) #ближняя лапка слева
	ellipse (screen, (0, 0, 0), (x + x1 / 2, y + y1 - 3 * r / 5, x1 / 2, y1 / 5), 1)

	circle (screen, (0, 255, 255), (xe + x1, ye + 4 * r - 2 * re), re) #глаза
	circle (screen, (0, 0, 0), (xe + x1, ye + 4 * r - 2 * re), re, 1)
	circle (screen, (0, 255, 255), (2 * x - xe + x1, ye + 4 * r - 2 * re), re) 
	circle (screen, (0, 0, 0), (2 * x - xe + x1, ye + 4 * r - 2 * re), re, 1)

	ellipse (screen, (0, 0, 0), (xe + x1 - re / 2, ye + 4 * r - 3 * re, re, 2 * re)) #зрачки
	ellipse (screen, (0, 0, 0), (2 * x - xe + x1 - re / 2, ye + 4 * r - 3 * re, re, 2 * re))

	polygon (screen, (245, 222, 179), ((x + x1, y + re + 2 * r), (x - re + x1, y - re + 2 * r), (x + re + x1, y - re + 2 * r))) #нос
	polygon (screen, (0, 0, 0), ((x + x1, y + re + 2 * r), (x - re + x1, y - re + 2 * r), (x + re + x1, y - re + 2 * r)), 1)

	polygon (screen, (210, 105, 30), ((x - r + x1, y + r), (x - r + re + x1, y + 3 * re + r), (x - r + 2 * re + x1, y + 2 * re + r))) #ухо Л
	polygon (screen, (0, 0, 0), ((x - r + x1, y + r), (x - r + re + x1, y + 3 * re + r), (x - r + 2 * re + x1, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x - r + 1 + x1, y + r + 1), (x - r + re - 1 + x1, y + 3 * re + r - 1), (x - r + 2 * re - 1 + x1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x - r + 1 + x1, y + r + 1), (x - r + re + x1, y + 3 * re + r - 1), (x - r + 2 * re - 1 + x1, y + 2 * re + r)), 1)

	polygon (screen, (210, 105, 30), ((x + r + x1, y + r), (x + r - re + x1, y + 3 * re + r), (x + r - 2 * re + x1, y + 2 * re + r))) #ухо П
	polygon (screen, (0, 0, 0), ((x + r + x1, y + r), (x + r - re + x1, y + 3 * re + r), (x + r - 2 * re + x1, y + 2 * re + r)), 1)
	polygon (screen, (222, 184, 135), ((x + r - 1 + x1, y + r + 1), (x + r - re + x1, y + 3 * re + r - 1), (x + r - 2 * re + 1 + x1, y + 2 * re + r))) #внут
	polygon (screen, (0, 0, 0), ((x + r - 1 + x1, y + r + 1), (x + r - re + x1, y + 3 * re + r - 1), (x + r - 2 * re + 1 + x1, y + 2 * re + r)), 1)

	line (screen, (0, 0, 0), (x + x1, y + re + 2 * r), (x + x1, y + 2 * re + 2 * r), 1) #рот
	arc (screen, (0, 0, 0), (x + x1, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)
	arc (screen, (0, 0, 0), (x - 2 * re + x1, y + 2 * r + re, 2 * re, 2 * re), 10, 6, 1)

	arc (screen, (105, 105, 105), (x + x1, y + 2 * r, r, 3 * re), 1, 3, 1) #усы
	arc (screen, (105, 105, 105), (x + x1, y + 2 * r + re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x + x1, y + 2 * r + 2 * re, r, 3 * re), 1, 3, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r + re, r, 3 * re), 0.5, 2.5, 1)
	arc (screen, (105, 105, 105), (x - r + x1, y + 2 * r + 2 * re, r, 3 * re), 0.5, 2.5, 1)

KisaOL (50, 450, 90, 60, 15, 43, 475, 3) #Киса1

KisaOL (540, 900, 60, 40, 10, 537, 915, 2)

KisaBL (390, 520, 200, 100, 30, 405, 570, 6)

KisaBR (410, 720, 200, 100, 25, 420, 670, 6)

KisaBR (110, 900, 140, 70, 20, 120, 860, 4)

KisaOR (60, 720, 200, 100, 25, 70, 670, 6)

KisaOR (60, 620, 140, 70, 20, 70, 580, 4)



#def zrach1 (x, y, r, n, L):
#	for i in range (n - L):
#		circle (screen, (255, 255, 255), (x + i, y + i), r - 2)
#
#zrach1 (40, 475, 3, 5, 1)
#zrach1 (54, 475, 3, 5, 1)
#
#def zrach2 (x, y, r, n, L):
#	for i in range (n - L, L):
#		circle (screen, (255, 255, 255), (x + i, y + i), r)
#
#zrach2 (40, 475, 1, 5, 1)
#zrach2 (54, 475, 1, 5, 1)
#
#
#def zrach3 (x, y, r, n, L):
#	for i in range (L, n):
#		circle (screen, (255, 255, 255), (x + i, y + i), r - 2)
#
#zrach3 (40, 475, 3, 5, 1)
#zrach3 (54, 475, 3, 5, 1)




def zrach (x, y, n):
		line (screen, (255, 255, 255), (x, y), (x + n, y + n), 1)

zrach (41, 473, 3) #1
zrach (55, 473, 3)


zrach (535, 913, 1) #2
zrach (541, 913, 1)


zrach (372, 566, 6) #3
zrach (402, 566, 6)


zrach (595, 754, 5) #4
zrach (617, 754, 5)


zrach (238, 930, 3) #5
zrach (256, 930, 3)


zrach (248, 754, 5) #6
zrach (268, 754, 5)

zrach (188, 649, 3) #7
zrach (208, 649, 3)


#KisaOL (50, 450, 90, 60, 15, 43, 475, 3) #Киса1

#KisaOL (540, 900, 60, 40, 10, 537, 915, 2) #Киса2

#KisaBL (390, 520, 200, 100, 30, 405, 570, 6) #Киса3

#KisaBR (410, 720, 200, 100, 25, 420, 670, 6) #Киса4

#KisaBR (110, 900, 140, 70, 20, 120, 860, 4) #Киса5

#KisaOR (60, 720, 200, 100, 25, 70, 670, 6) #Киса6

#KisaOR (60, 620, 140, 70, 20, 70, 580, 4) #Киса7



#ограничения : x1/10, y1/10, r/5, re/2


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()