from Config import *
import pygame, random, math
pygame.init()

## TODO: Apples, Sell apples, Buy seeds, Trees die after 2 apples

class Player:
    Seeds = 5
    Money = 0
    Apples = 0

class Plant:
    def __init__(self, Pos):
        self.Pos = Pos
        self.Progress = 0
        self.Img = pygame.image.load("Plant1.png")

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

Trees = []
while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 60, 1), pygame.Rect(0, 350, 1000, 150))
    pygame.draw.rect(screen, (0, 128, 200), pygame.Rect(0, 0, 1000, 350))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and Player.Seeds != 0:
            MousePos = pygame.mouse.get_pos()
            Trees.append(Plant((MousePos[0]-math.floor(pygame.image.load("Plant1.png").get_size()[0]/2), 125)))
            Player.Seeds = Player.Seeds - 1

    for i in range(len(Trees)):
        screen.blit(Trees[i].Img, Trees[i].Pos)
        Trees[i].Img = pygame.image.load(f"Plant{round(Trees[i].Progress/25) if round(Trees[i].Progress/25) != 0 else 1}.png")
        Trees[i].Progress = Trees[i].Progress + 1/60
        
    pygame.display.flip()
    clock.tick(60) #60fps
