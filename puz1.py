import pygame
import math
import random
pygame.init()

#colors
RED = (255,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
LIMEGREEN =(50,205,50)
GREEN = (0,128,0)
BLUE = (0,0,255)
SKYBLUE = (135,206,235)
LIGHTBLUE =(173,216,230)
INDIGO = (75,0,130)
PURPLE = (128,0,128)
WHITE = (255,255,255)
BLACK = (0,0,0) 
colors = [RED, ORANGE, YELLOW, LIMEGREEN, GREEN, BLUE, SKYBLUE, LIGHTBLUE, INDIGO, PURPLE, WHITE, BLACK]

#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
screen.fill(WHITE)
clock = pygame.time.Clock()


puzzle = []
for i in range(6):
    puzzle.append([])
    for j in range(4):
        c = random.randint(0,len(colors)-1)
        col = colors[c]
        puzzle[i].append([pygame.Rect(i*100,j*100,100,100),col])
print(puzzle)

#MAIN
done = False
while not done:
    clock.tick(25)
    screen.fill(WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
            
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            col = puzzle[i][j][1]
            pygame.draw.rect(screen, col, puzzle[i][j][0], 0)
            
    pygame.display.flip()
pygame.quit()

