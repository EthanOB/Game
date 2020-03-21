from Config import *
import pygame, random
pygame.init()

#def PlantGrowImage(grow):
#    if grow <= 25
#       Num = 1
 #  elif grow <= 50
#       Num = 3
 #  elif grow<= 75
#       Num = 4
 #  elif grow <= 100
#       Num = 6
 #  return pygame.image.load(f"Plant{Num}.png")

class Tree:
    def __init__(self, Pos):
        self.Pos = Pos
        self.Img = pygame.image.load("Plant6.png")

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

Plant = Tree((0, 0))

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 60, 1), pygame.Rect(0, 350, 1000, 150))
    pygame.draw.rect(screen, (0, 128, 200), pygame.Rect(0, 0, 1000, 350))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            Plant = Tree((MousePos[0], 125))
    screen.blit(Plant.Img, Plant.Pos)

    pygame.display.flip()
    clock.tick(60)
