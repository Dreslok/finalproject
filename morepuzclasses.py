import pygame
import math
import random
import operator
import colors
pygame.init()


purples = [colors.lavender, colors.thistle, colors.plum, colors.orchid, colors.violet, colors.magenta, colors.mediumorchid, colors.darkorchid, colors.darkviolet, colors.blueviolet, colors.darkmagenta, colors.purple, colors.mediumpurple, colors.mediumslateblue, colors.slateblue, colors.darkslateblue]

#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PUZZLES!!!!!!!!!!!!!!!!")
screen.fill(colors.WHITE)
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
            



class Puzzle():
    def __init__(self, x, y, pwidth, pheight, solved):
        self.x = x
        self.y = y
        self.pwidth = pwidth
        self.pheight = pheight
        self.puzzle = []
        self.solved = solved
        self.selectedlist = []
        self.c = 0
        for i in range(self.x):
            self.puzzle.append([])
            for j in range(self.y):
                col = purples[self.c % len(purples)]
                if i == 0 and j == 0:
                    self.puzzle[i].append(PuzzlePiece(i, j, (j*self.pwidth, i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, True, False, True, False, False))
                elif i == 0 and j == (self.y-1):
                    self.puzzle[i].append(PuzzlePiece(i, j, (j*self.pwidth, i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, True, False, False, True, False))
                elif i == (self.x - 1) and j == 0:
                    self.puzzle[i].append(PuzzlePiece(i, j, (j*self.pwidth, i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, False, True, True, False, False))
                elif i == (self.x - 1) and j == (self.y - 1):
                    self.puzzle[i].append(PuzzlePiece(i, j, (j*self.pwidth, i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, False, True, False, True, False))
                elif j == 0:
                    self.puzzle[i].append(PuzzlePiece(i, j,(j*self.pwidth,i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col,  True, False, False, False, False))
                elif j == (self.y - 1):
                    self.puzzle[i].append(PuzzlePiece(i, j,(j*self.pwidth,i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col,  False, True, False, False, False))
                elif i == 0:
                    self.puzzle[i].append(PuzzlePiece(i, j,(j*self.pwidth,i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, False, False, True, False, False))
                elif i == (self.x - 1):
                    self.puzzle[i].append(PuzzlePiece(i, j,(j*self.pwidth,i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, False, False, False, True, False))
                else:
                    self.puzzle[i].append(PuzzlePiece(i, j,(j*self.pwidth,i*self.pheight), (j*self.pwidth, i*self.pheight), (self.pwidth, self.pheight), col, False, False, False, False, True))
                self.c += 1   
    
    def randomize(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                rand1 = random.randint(0, size[0]-self.pwidth)
                rand2 = random.randint(0, size[1]-self.pheight)
                self.puzzle[i][j].pos = (rand1, rand2)
                
    def drawPuz(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                self.puzzle[i][j].drawPiece()
                
    def movePuz(self):
        if pygame.mouse.get_pressed()[0]:
            a, b = pygame.mouse.get_pos()
            for i in range(len(self.puzzle)):
                for j in range(len(self.puzzle[i])):
                    if not self.puzzle[i][j].isInPlace():
                        c, d = self.puzzle[i][j].pos
                        e, f = self.puzzle[i][j].outerpos
                        g, h = self.puzzle[i][j].originalpos
                        if a >= c and a <= e and b >= d and b <= f:
                            if len(self.selectedlist) < 2:
                                self.selectedlist.append(self.puzzle[i][j])
        else:
            for i in self.selectedlist:
                self.selectedlist.remove(i)
        if len(self.selectedlist) > 1:
            self.selectedlist[0].movePiece(pygame.mouse.get_pos())
        
            
    def checksolved(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                a, b = self.puzzle[i][j].pos
                c, d = self.puzzle[i][j].originalpos
                if a != b or c != d:
                    return False
        return True
    
    def solve(self):
        if not self.solved:
            for i in range(len(self.puzzle)):
                for j in range(len(self.puzzle[i])):
                    self.puzzle[i][j].pos == self.puzzle[i][j].originalpos
        self.solved = self.checksolved()

puz = Puzzle(4, 4, 100, 100, False)
puz.randomize()
#puz.solve()


done = False
while not done:
    clock.tick(25)
    screen.fill(colors.WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            puz.solve()
        if event.key == pygame.K_r:
            puz.randomize()
    if event.type == pygame.MOUSEBUTTONDOWN:
        a, b = pygame.mouse.get_pos()
        for i in range(len(puz.puzzle)):
            for j in range(len(puz.puzzle[i])):
                if not puz.puzzle[i][j].isInPlace():
                    c, d = puz.puzzle[i][j].pos
                    e, f = puz.puzzle[i][j].outerpos
                    g, h = puz.puzzle[i][j].originalpos
                    if a >= c and a <= e and b >= d and b <= f:
                        if len(puz.selectedlist) < 2:
                            puz.selectedlist.append(puz.puzzle[i][j])
    else:
        for i in puz.selectedlist:
            puz.selectedlist.remove(i)
    if len(puz.selectedlist) > 1:
        puz.selectedlist[0].movePiece(pygame.mouse.get_pos())
    
    puz.drawPuz()
    
            


    pygame.display.flip()
pygame.quit()

