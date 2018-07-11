import pygame
from pygame.locals import *
from CONST import *
import Map

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

sky = pygame.image.load("Graphics/sky.png")
Sky = window.blit(sky,(0,0))

map = Map.Map(window)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
