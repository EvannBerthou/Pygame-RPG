import pygame
from pygame.locals import *
from math import hypot

pygame.init()

## TODO: MOVE ALL VARS IN GLOBALS

class Globals:
    window = None
    playerX = 0
    core = None
    deltaTime = 0

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 800

TILE_SIZE = 16

#COLORS
COLOR_BLACK = (0,0,0,255)
COLOR_WHITE = (255,255,255,255)
COLOR_RED = (255,0,0,255)
COLOR_GREEN = (0,255,0,255)
COLOR_BLUE = (0,0,255,255)


#TILES
DIRT = "Graphics/dirt.jpg"
STONE = "Graphics/stone.jpg"
WOOD = "Graphics/wood.jpg"
SKY = "Graphics/sky.png"
PLAYER_LEFT = "Graphics/player_left.png"
PLAYER_RIGHT = "Graphics/player_right.png"


#PLAYER
PlayerSpeed = .15
RegenSpeed = 1/32

#Functions
def Clamp(value, min, max):
    if value > max:
        value = max
    if value < min:
        value = min
    return value

def Distance(x1,y1,x2,y2):
    return hypot(x2 - x1, y2 - y1)


#KEYS
KEY_LEFT = pygame.K_q
KEY_RIGHT = pygame.K_d

#FONTS
fps_font = pygame.font.SysFont("Arial", 16)
Damage_font = pygame.font.SysFont("monospace",18)
Wave_font = pygame.font.SysFont("monoscpace",22)
