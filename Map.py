import pygame
from CONST import *
from PIL import Image

class Map:
    def DrawTile(self,x,y,TILE):
        tile = pygame.image.load(TILE)
        tile = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))
        self.window.blit(tile,(x,y))

    def __init__(self, window):
        self.window = window

        im = Image.open('Graphics/Map.png')
        pix = im.load()
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if pix[x,y][3] is not 0:
                    if pix[x,y] in TILES:
                        self.DrawTile(x * TILE_SIZE, y * TILE_SIZE, TILES[pix[x,y]])
                    else:
                        print("{} not defined".format(pix[x,y]))
