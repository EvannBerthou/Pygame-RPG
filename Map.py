import pygame
from CONST import *
from PIL import Image

pygame.init()

class Map:

    def LoadTexture(file):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (TILE_SIZE, TILE_SIZE))
        surface = pygame.Surface((TILE_SIZE,TILE_SIZE), pygame.HWSURFACE | pygame.SRCALPHA)
        surface.blit(bitmap,(0,0))
        return surface

    Dirt = LoadTexture(DIRT)
    Stone = LoadTexture(STONE)
    Wood = LoadTexture(WOOD)
    Player = LoadTexture(PLAYER)

    def GetTileFromColor(Color):
        TILES = dict([(COLOR_RED, Map.Dirt),(COLOR_BLUE,Map.Wood), (COLOR_GREEN, Map.Stone)])
        return TILES[Color]

    def DrawTile(self,x,y,Tile):
        self.window.blit(Tile, (x,y))


    def GetMap(self):
        map = Image.open("Graphics/Map.png")
        return map.load(), map.size

    def draw(self, PlayerX,PlayerY):
        for x in range(self.mapSize[0]):
            for y in range(self.mapSize[1]):
                if self.pix[x,y][3] is not 0:
                    self.DrawTile(x * TILE_SIZE - PlayerX, y * TILE_SIZE + PlayerY, Map.GetTileFromColor(self.pix[x,y]))

    def __init__(self, window):
        self.window = window
        self.pix, self.mapSize = self.GetMap()
