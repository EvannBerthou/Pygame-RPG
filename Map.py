from CONST import *
from PIL import Image
from Core import *
import math

pygame.init()

class Pix:
    def __init__(self,x,y,TILE, collide):
        self.x = x
        self.y = y
        self.tile = TILE
        self.collide = collide

    def ShouldShow(self, playerX, playerY):
        dist = (self.x * TILE_SIZE - playerX - WINDOW_WIDTH)**2
        return dist < (WINDOW_WIDTH + 16)**2


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

    TILES = dict([(COLOR_RED, Dirt),(COLOR_BLUE,Wood), (COLOR_GREEN, Stone)])

    def DrawTile(self,x,y,Tile):
        Globals.window.blit(Tile, (x,y))

    def GetCollsionAt(self, x,y):
        for pix in self.pix:
            if pix.collide:
                if pix.x is x and pix.y is y:
                    return True
        return False

    def GetMap(self):
        map = Image.open("Graphics/Map.png")
        pix = map.load()
        Tiles = []

        for x in range(map.size[0]):
            for y in range(map.size[1]):
                if pix[x,y][3] is not 0:
                    Tiles.append(Pix(x,y, Map.TILES[pix[x,y]], not pix[x,y][0] is 100))

        return Tiles, map.size

    def draw(self, PlayerX):
        for tile in self.pix:
            if tile.ShouldShow(PlayerX, 0):
                self.DrawTile(tile.x * TILE_SIZE - int(PlayerX),tile.y * TILE_SIZE,tile.tile)

    def __init__(self, window):
        Globals.window = window
        self.pix,self.mapSize = self.GetMap()
        self.draw(0)

        core = Core(self.mapSize[0] / 2 , WINDOW_HEIGHT / TILE_SIZE - 6) #Place the core in the center of the map
        self.pix.append(Pix(core.x, core.y, Map.Wood, False))
