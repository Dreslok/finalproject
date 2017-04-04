import pygame
import math
import random
import operator
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
colors = [RED, DEEPPINK, ORANGE, GOLD, YELLOW, YELLOWGREEN, LIMEGREEN, GREENYELLOW, GREEN, AQUA, BLUE, SKYBLUE, LIGHTBLUE, INDIGO, PURPLE]

#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
screen.fill(WHITE)
clock = pygame.time.Clock()

pwidth = 100
pheight = 100

class PuzzlePiece():
    def __init__(self, x, y, pos, psize, color, isleftpiece, isrightpiece, istoppiece, isbottompiece, iscenterpiece, isleftconnected, isrightconnected, istopconnected, isbottomconnected):
        self.x = x
        self.y = y
        self.pos = pos
        self.outerpos = tuple(sum(i) for i in zip(pos, psize))
        self.psize = psize
        self.color = color
        self.isleftpiece = isleftpiece
        self.isrightpiece = isrightpiece
        self.istoppiece = istoppiece
        self.isbottompiece = isbottompiece
        self.iscenterpiece = iscenterpiece
        self.isleftconnected = isleftconnected
        self.isrightconnected = isrightconnected
        self.istopconnected = istopconnected
        self.isbottomconnected = isbottomconnected 
        
    
    def drawPiece(self):
        pygame.draw.rect(screen, self.color, (self.pos, self.psize), 0)
    def movePiece(self, newxy):
        self.pos = newxy



#def checkOverlap(piece1, piece2, newxy):
    #if piece1.x != piece2.x or piece1.y != piece2.y:
        #piece1.movePiece(newxy)

c = 0
col = c
puzzle = []

columns = 10
rows = 7


for i in range(rows):
    puzzle.append([])
    x = i
    for j in range(columns):
        y = j
        if i == 0 and j == 0:
            col = BLACK
            puzzle[i].append(PuzzlePiece(x,y,(y*pwidth,x*pheight),(pwidth, pheight), col, True, False, True, False, False, False, False, False, False))
        elif i == 0 and j == (columns - 1):
            col = BLACK
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col, True, False, False, True, False, False, False, False, False))
        elif i == (rows - 1) and j == 0:
            col = BLACK
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col, False, True, True, False, False, False, False, False, False)) 
        elif i == (rows - 1) and j == (columns - 1):
            col = BLACK
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col, False, True, False, True, False, False, False, False, False))             
        elif j == 0:
            col = VIOLET
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col,  True, False, False, False, False, False, False, False, False))
        elif j == (columns - 1):
            col = VIOLET
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col,  False, True, False, False, False, False, False, False, False))
        elif i == 0:
            col = VIOLET
            puzzle[i].append(PuzzlePiece(x, y, (y*pwidth,x*pheight),(pwidth, pheight), col, False, False, True, False, False, False, False, False, False))
        elif i == (rows - 1):
            col = VIOLET
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col, False, False, False, True, False, False, False, False, False))
        else:
            col = colors[c % len(colors)]            
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (pwidth, pheight), col, False, False, False, False, True, False, False, False, False))
        c += 1
# i, j, width, height, color, connected
#leftedge, rightedge, topedge, bottomedge
#connectedleft, connectedright, connectedtop, connectedbottom

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(str(puzzle[i][j].x), end = ',')
        print(str(puzzle[i][j].y), end = '   ')
    print(' ')
done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]:
        print(pygame.mouse.get_pos())
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if pygame.mouse.get_pos() >= puzzle[i][j].pos and pygame.mouse.get_pos() <= puzzle[i][j].outerpos:
                    puzzle[i][j].movePiece(pygame.mouse.get_pos())
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j].drawPiece()
    

            
    pygame.display.flip()
pygame.quit()

#mouse pushed down take note of which piece it's currently over, save into a variable
#mouse released/up clear variable
#then use mouse drag event to check variable if it's a piece