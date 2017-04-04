import pygame
import math
import random
pygame.init()

#colors
RED = (255,0,0)
DEEPPINK = (255,20,147)
ORANGE = (255,165,0)
GOLD = (255,215,0)
YELLOW = (255,255,0)
YELLOWGREEN = (104,205,0)
LIMEGREEN =(50,205,50)
GREENYELLOW = (173,255,47)
GREEN = (0,128,0)
AQUA = (0,255,255)
BLUE = (0,0,255)
SKYBLUE = (135,206,235)
LIGHTBLUE =(173,216,230)
INDIGO = (75,0,130)
PURPLE = (128,0,128)
VIOLET = (238,130,238)
WHITE = (255,255,255)
BLACK = (0,0,0) 
colors = [RED, DEEPPINK, ORANGE, GOLD, YELLOW, YELLOWGREEN, LIMEGREEN, GREENYELLOW, GREEN, AQUA, BLUE, SKYBLUE, LIGHTBLUE, INDIGO, PURPLE, VIOLET, BLACK]

#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
screen.fill(WHITE)
clock = pygame.time.Clock()

pwidth = 100
pheight = 100
c = 0
col = c
puzzle = []

columns = 6
rows = 4

isupperleftcorner = [True, False, True, False]
isupperrightcorner = [True, False, False, True]
isbottomleftcorner = [False, True, True, False]
isbottomrightcorner = [False, True, False, True]

isleftpiece = [True, False, False, False]
isrightpiece = [False, True, False, False]
istoppiece = [False, False, True, False]
isbottompiece = [False, False, False, True]

iscenterpiece = [False, False, False, False]

for i in range(rows):
    puzzle.append([])
    x = i
    for j in range(columns):
        y = j
        col = colors[c % len(colors)]
        if i == 0 and j == 0:
            puzzle[i].append([x, y, pwidth, pheight, col, isupperleftcorner, False, False, False, False])
        elif i == 0 and j == (columns - 1):
            puzzle[i].append([x, y, pwidth, pheight, col, isupperrightcorner, False, False, False, False])
        elif i == (rows - 1) and j == 0:
            puzzle[i].append([x, y, pwidth, pheight, col, isbottomleftcorner, False, False, False, False]) 
        elif i == (rows - 1) and j == (columns - 1):
            puzzle[i].append([x, y, pwidth, pheight, col, isbottomrightcorner, False, False, False, False])             
        elif j == 0:
            puzzle[i].append([x, y, pwidth, pheight, col,  isleftpiece, False, False, False, False])
        elif j == (columns - 1):
            puzzle[i].append([x, y, pwidth, pheight, col,  isrightpiece, False, False, False, False])
        elif i == 0:
            puzzle[i].append([x, y, pwidth, pheight, col, istoppiece, False, False, False, False])
        elif i == (rows - 1):
            puzzle[i].append([x, y, pwidth, pheight, col, isbottompiece, False, False, False, False])
        else:
            puzzle[i].append([x, y, pwidth, pheight, col, iscenterpiece, False, False, False, False])
        c += 1

# i, j, width, height, color, connected
#leftedge, rightedge, topedge, bottomedge
#connectedleft, connectedright, connectedtop, connectedbottom

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(str(puzzle[i][j]), end = ',')
    print(' ')
done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
            
    
    #for i in range(len(puzzle)):
        #for j in range(en(puzzle[i])):
            
            

            
    pygame.display.flip()
pygame.quit()

