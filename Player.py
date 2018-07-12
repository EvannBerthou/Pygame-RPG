from CONST import *
import pygame
from Map import *

class Player:
    def draw(self):
        x = WINDOW_WIDTH / 2

        sprite = Map.Player_left
        if self.velocity is not 0:
            sprite = Map.Player_right if self.velocity is 1 else Map.Player_left
        else:
            sprite = self.lastSprite

        self.lastSprite = sprite

        self.window.blit(sprite,(x,self.y))


        pygame.draw.rect(self.window, COLOR_WHITE, (50,10,100,10), 1)
        self.health = Clamp(self.health,0,self.maxHealth)
        healthRatio = self.health / self.maxHealth
        pygame.draw.rect(self.window, COLOR_GREEN, (51,11, int(98 * healthRatio), 8))


    def move(self, deltaTime,mapSize):
        self.health += deltaTime / 32
        self.CanMoveLeft = not self.map.GetTileAtCoord(int(self.x / TILE_SIZE + 25), int(self.y / TILE_SIZE))
        self.CanMoveRight = not self.map.GetTileAtCoord(int(self.x / TILE_SIZE + 26), int(self.y / TILE_SIZE))

        if (self.velocity is 1 and self.CanMoveRight) or (self.velocity is -1 and self.CanMoveLeft):
            self.x += self.velocity * PlayerSpeed * deltaTime

        mapX = (mapSize[0] * TILE_SIZE) - (WINDOW_WIDTH / 2) - TILE_SIZE

        self.x = Clamp(self.x, -400, mapX)


        # print(int(self.x / TILE_SIZE + 25))
        # print(self.y / TILE_SIZE + 1)
        if not self.map.GetTileAtCoord(int(self.x / TILE_SIZE + 25),int(self.y / TILE_SIZE + 1)):
            self.y += 1

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

    def __init__(self, window, map):
        self.x = 0
        self.y = WINDOW_HEIGHT - 6 * TILE_SIZE
        self.window = window
        self.velocity = 0

        self.map = map

        self.maxHealth = 100
        self.health = 0

        self.lastSprite = Map.Player_left

        self.CanMoveLeft = True
        self.CanMoveRight = True

        self.draw()
