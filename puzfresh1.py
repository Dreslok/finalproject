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
rows = 4
columns = 4


class Puzzle():
    def __init__(self, groups):
        self.groups = groups
        
class GroupedPieces():
    def __init__(self, pieces):
        self.pieces = pieces

class Piece():
    def __init__(self, x, y, originalpos, currentpos, size, isleft, isright, istop, isbottom, group):
        self.x = x
        self.y = y
        self.originalpos = originalpos
        self.currentpos = currentpos
        self.size = size
        self.isleft = isleft
        self.isright = isright
        self.istop = istop
        self.isbottom = isbottom
        self.group = group

done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True

    pygame.display.flip()
pygame.quit()
