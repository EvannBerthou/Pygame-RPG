import pygame
from CONST import *
from PIL import Image

pygame.init()

class Pix:
    def __init__(self,x,y,TILE):
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.tile = TILE

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
    Player_left = LoadTexture(PLAYER_LEFT)
    Player_right = LoadTexture(PLAYER_RIGHT)

    TILES = dict([(COLOR_RED, Dirt),(COLOR_BLUE,Wood), (COLOR_GREEN, Stone)])

    def DrawTile(self,x,y,Tile):
        self.window.blit(Tile, (x,y))


    def GetMap(self):
        map = Image.open("Graphics/Map.png")
        pix = map.load()
        Tiles = []
        for x in range(map.size[0]):
            for y in range(map.size[1]):
                if pix[x,y][3] is not 0:
                    Tiles.append(Pix(x,y, Map.TILES[pix[x,y]]))

        return Tiles, map.size

    def draw(self, PlayerX,PlayerY):
        for tile in self.pix:
            self.DrawTile(tile.x - PlayerX,tile.y,tile.tile)

    def __init__(self, window):
        self.window = window
        self.pix,self.mapSize = self.GetMap()
        self.draw(0,0)
