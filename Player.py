from CONST import *
import pygame

class Player:
    def draw(self):
        x = WINDOW_WIDTH / 2
        self.window.blit(self.sprite,(x,self.y))

    def move(self, deltaTime,mapSize):
        self.x += self.velocity * PlayerSpeed * deltaTime
        mapX = (mapSize[0] * TILE_SIZE) - (WINDOW_WIDTH / 2) - TILE_SIZE

        if self.x > mapX:
            self.x = mapX
        if self.x < -400:
            self.x = -400

    def handle_event(self,event):
        if event.type is pygame.KEYDOWN:

            if event.key is pygame.K_a:
                self.velocity = -1

            if event.key is pygame.K_d:
                self.velocity = 1

        if event.type is pygame.KEYUP:
            if event.key in [pygame.K_d, pygame.K_a]:
                self.velocity = 0

    def __init__(self, window,x,sprite):
        self.x = x
        self.y = WINDOW_HEIGHT - 6 * TILE_SIZE
        self.window = window
        self.velocity = 0
        self.sprite = sprite
        self.health = 0
        self.draw()
