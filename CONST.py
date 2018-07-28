import pygame
from pygame.locals import *
from math import hypot

pygame.init()

class Globals:
    window = None
    player = None
    core = None
    
    playerX = 0
    playerY = 0
    deltaTime = 0
    mapX = 0

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

def Distance(x1,x2,y1,y2):
    return hypot(x2 - x1, y2 - y1)


#KEYS
KEY_LEFT = pygame.K_q
KEY_RIGHT = pygame.K_d

#FONTS
Default_font = pygame.font.get_default_font()
fps_font = pygame.font.SysFont("Arial", 16)
NewWave_font = pygame.font.SysFont("Arial",20, bold=True)
Damage_font = pygame.font.SysFont(Default_font,26)
Wave_font = pygame.font.SysFont(Default_font,22)
