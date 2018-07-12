from CONST import *
import pygame
from Map import *

class Player:
    def draw(self):
        Map
        x = WINDOW_WIDTH / 2

        if self.velocity is 1:
            sprite = Map.Player_right
        else:
            sprite = Map.Player_left

        self.window.blit(sprite,(x,self.y))


        pygame.draw.rect(self.window, COLOR_WHITE, (25,10,100,10), 1)
        self.health = Clamp(self.health,0,self.maxHealth)
        healthRatio = self.health / self.maxHealth
        pygame.draw.rect(self.window, COLOR_GREEN, (26,11, int(98 * healthRatio), 8))


    def move(self, deltaTime,mapSize):
        self.x += self.velocity * PlayerSpeed * deltaTime
        mapX = (mapSize[0] * TILE_SIZE) - (WINDOW_WIDTH / 2) - TILE_SIZE

        self.x = Clamp(self.x, -400, mapX)

        self.health += deltaTime / 32

    def handle_event(self,event):
        keys = pygame.key.get_pressed()
        if event.type is pygame.KEYDOWN:
            if self.velocity is 0:
                if keys[pygame.K_a]:
                    self.velocity = -1
                if keys[pygame.K_d]:
                    self.velocity = 1

        if event.type == pygame.KEYUP:
            if self.velocity is 1 and event.key is pygame.K_d:
                self.velocity = 0
            if self.velocity is -1 and event.key is pygame.K_a:
                self.velocity = 0

    def __init__(self, window):
        self.x = 0
        self.y = WINDOW_HEIGHT - 6 * TILE_SIZE
        self.window = window
        self.velocity = 0

        self.maxHealth = 100
        self.health = 0

        self.draw()
