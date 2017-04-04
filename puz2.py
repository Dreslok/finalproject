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


puzzle = []
c = 0
for i in range(4):
    puzzle.append([])
    for j in range(4):
        puzzle[i].append([pygame.Rect(i*100,j*100,100,100),[i,j]])

def randomize(puz):
    puz2 = []
    for i in range(len(puz)):
        puz2.append([])
        for j in range(len(puz[i])):
            rand1 = random.randint(0,size[0]-100)
            rand2 = random.randint(0,size[1]-100)
            puz2[i].append([pygame.Rect(rand1,rand2,100,100),puz[i][j][1]])
    return puz2

def drawPuz(puz):
    c = 0
    for i in range(len(puz)):
        for j in range(len(puz[i])):
            col = colors[c % len(colors)]
            pygame.draw.rect(screen, col, puz[i][j][0], 0)
            c += 1
            
ranpuz = randomize(puzzle)
#MAIN
done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
            

    #drawPuz(puzzle)
    drawPuz(ranpuz)
            
    pygame.display.flip()
pygame.quit()

