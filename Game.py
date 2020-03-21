import Config
import pygame

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

gameDisplay = pygame.display.set_mode((200,200))

pygame.display.set_caption('Tree Game')
while True: # main game loop
    gameDisplay.fill((0,0,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
