import pygame
import math
import random
import operator
import colors
pygame.init()

#colors
RED = colors.Red
DEEPPINK = colors.DeepPink
ORANGE = colors.Orange
GOLD = colors.Gold
YELLOW = colors.Yellow
YELLOWGREEN = colors.YellowGreen
LIMEGREEN = colors.LimeGreen
GREENYELLOW = colors.GreenYellow
GREEN = colors.Green
AQUA = colors.Aqua
BLUE = colors.Blue
SKYBLUE = colors.SkyBlue
LIGHTBLUE = colors.LightBlue
INDIGO = colors.Indigo
PURPLE = colors.Purple
VIOLET = colors.Violet
WHITE = colors.White
BLACK = colors.Black
colors = [RED, DEEPPINK, ORANGE, GOLD, YELLOW, GREENYELLOW, YELLOWGREEN, LIMEGREEN, GREEN, BLUE, AQUA, SKYBLUE, LIGHTBLUE, VIOLET, INDIGO, PURPLE]

#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
screen.fill(WHITE)
clock = pygame.time.Clock()

pwidth = 100
pheight = 100

class PuzzlePiece():
    def __init__(self, x, y, originalpos, pos, psize, color, isleftpiece, isrightpiece, istoppiece, isbottompiece, iscenterpiece):
        self.x = x
        self.y = y
        self.originalpos = originalpos
        self.pos = pos
        self.outerpos = tuple(sum(i) for i in zip(pos, psize))
        self.psize = psize
        self.color = color
        self.isleftpiece = isleftpiece
        self.isrightpiece = isrightpiece
        self.istoppiece = istoppiece
        self.isbottompiece = isbottompiece
        self.iscenterpiece = iscenterpiece
        self.hasbeenmoved = False
        self.isleftconnected = False
        self.isrightconnected = False
        self.istopconnected = False
        self.isbottomconnected = False 
        
    def isInPlace(self):
        a, b = self.pos
        c, d = self.originalpos
        e, f = self.psize
        if self.hasbeenmoved and a >= (c-5) and a <= (c + e + 5) and b >= (d-5) and b <= (d+f+5):
            return True
        else:
            return False
        
    def drawPiece(self):
        pygame.draw.rect(screen, self.color, (self.pos, self.psize), 0)
        
    def movePiece(self, newxy):
        if self.isInPlace():
            self.pos = self.originalpos
        else:
            self.pos = newxy
            self.outerpos = tuple(sum(i) for i in zip(self.pos, self.psize))
            self.hasbeenmoved = True
            
    def checkLeftConnection(self, left):
        a, b = self.pos
        c, d = left.outerpos
        if a >= c-5 and a <= c+5 and b >= d-5 and b <= d+5:
            self.isleftconnected = True
            left.isrightconnected = True
    def checkRightConnection(self, right):
        a, b = self.outerpos
        c, d = right.pos
        if a >= c-5 and a <= c+5 and b >= d-5 and b <= d+5:
            self.isrightconnected = True
            right.isleftconnected = True        




#def checkOverlap(piece1, piece2, newxy):
    #if piece1.x != piece2.x or piece1.y != piece2.y:
        #piece1.movePiece(newxy)

c = 0
col = c
puzzle = []

columns = int((len(colors))/2)
rows = 4


for i in range(rows):
    puzzle.append([])
    x = i
    for j in range(columns):
        rand1 = random.randint(0,size[0]-100)
        rand2 = random.randint(0,size[1]-100)        
        y = j
        if i == 0 and j == 0:
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x,y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, True, False, True, False, False))
        elif i == 0 and j == (columns - 1):
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight),(rand1, rand2), (pwidth, pheight), col, True, False, False, True, False))
        elif i == (rows - 1) and j == 0:
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, False, True, True, False, False)) 
        elif i == (rows - 1) and j == (columns - 1):
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, False, True, False, True, False))             
        elif j == 0:
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col,  True, False, False, False, False))
        elif j == (columns - 1):
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col,  False, True, False, False, False))
        elif i == 0:
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y, (y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, False, False, True, False, False))
        elif i == (rows - 1):
            col = colors[c % len(colors)]  
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, False, False, False, True, False))
        else:
            col = colors[c % len(colors)]            
            puzzle[i].append(PuzzlePiece(x, y,(y*pwidth,x*pheight), (rand1, rand2), (pwidth, pheight), col, False, False, False, False, True))
        c += 1


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(str(puzzle[i][j].x), end = ',')
        print(str(puzzle[i][j].y), end = '   ')
    print(' ')
    
selectedlist = []

done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
            
    if pygame.mouse.get_pressed()[0]:
        #print(pygame.mouse.get_pos())
        a, b = pygame.mouse.get_pos()
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if not puzzle[i][j].isInPlace():
                    c, d = puzzle[i][j].pos
                    e, f = puzzle[i][j].outerpos
                    g, h = puzzle[i][j].originalpos
                    if a >= c and a <= e and b >= d and b <= f:
                        if len(selectedlist) < 2:
                            selectedlist.append(puzzle[i][j])
                            
    else:
        for i in selectedlist:
            selectedlist.remove(i)
    if len(selectedlist) > 1:
        selectedlist[0].movePiece(pygame.mouse.get_pos())


    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j].drawPiece()
    
    #c, d = a, b
    #a, b = b, a
    pygame.display.flip()
pygame.quit()

#mouse pushed down take note of which piece it's currently over, save into a variable
#mouse released/up clear variable
#then use mouse drag event to check variable if it's a piece


#