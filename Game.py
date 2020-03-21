import Config
import pygame

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

def Plant(x, y):
    DISPLAYSURF.blit(pygame.image.load('Plant1.png'), (x,y))

pygame.display.set_caption('Tree Game')
x = 0
y = 1
while True: # main game loop
    DISPLAYSURF.fill((0,0,200))
    Plant(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    x = x+1
    y = y +1
    pygame.display.update()
