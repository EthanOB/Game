from Config import *
import pygame, random, math
pygame.init()

class Player:
    Seeds = 5
    Apples = 0

class Plant:
    def __init__(self, Pos):
        self.Pos = Pos
        self.Progress = 0
        self.Apples = 0
        self.AppleList = []
        self.Img = pygame.image.load("Plant1.png")
        self.ApplePos = (math.floor(self.Pos[0]+self.Pos[0]/2), 50)

    class Apple:
        def __init__(self, Pos):
            self.Img = pygame.image.load("Apple.png")
            self.Pos = Pos


screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

Trees = []
Pop = []
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
        if event.type == pygame.KEYDOWN and Player.Apples > 0 and event.key == pygame.K_a:
            Player.Apples = Player.Apples - 1
            Player.Seeds = Player.Seeds + 1

    for i in range(len(Trees)):
        screen.blit(Trees[i].Img, Trees[i].Pos)

        if Trees[i].Apples < 2:
            Trees[i].Img = pygame.image.load(f"Plant{round(Trees[i].Progress/25) if round(Trees[i].Progress/25) != 0 else 1}.png")
            Trees[i].Progress = Trees[i].Progress + 1/10
            if Trees[i].Progress/25 > 4:
                Trees[i].AppleList.append(Trees[i].Apple(Trees[i].ApplePos))
                #for i2 in range(len(Trees[i].AppleList)):
                    #screen.blit(Trees[i].AppleList[i2].Img, Trees[i].ApplePos)
                Trees[i].Apples = Trees[i].Apples + 1
                Player.Apples = Player.Apples + 1
        else:
            Pop.append(Trees.index(Trees[i]))

    for i in range(len(Pop)):
        Pop.sort()
        Trees.pop(Pop[i])
        Pop = []

    pygame.display.flip()
    clock.tick(60) #60fps
