import * from Config
import pygame, time
pygame.init()

#Ethan:
#Learn how to draw stuff on the window
#Kaleb:
#Learn how to do time
#Set the ticks up

def Tick():


TicksPerMinute = 5
WaterBoost = 20

class Plant():
    def __init__(self):
        self.GrowthRate = 5
        self.AppleInterval = 100
        self.DeathScore = 200

        self.Growth = 0

    Plant1 = pygame.image.load('Plant1.png')
    Plant2 = pygame.image.load('Plant2.png')
    Plant3 = pygame.image.load('Plant3.png')
    Plant4 = pygame.image.load('Plant4.png')
    Plant5 = pygame.image.load('Plant5.png')
    Plant6 = pygame.image.load('Plant6.png')

class Player()
    def __init__(self):
        self.Seeds = 5
        self.Apples = 0
        self.Water = 5

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:


pygame.quit()
