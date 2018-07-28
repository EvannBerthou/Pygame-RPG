from CONST import *


#TODO : MOVE INTO PLAYER CLASS
def DrawPlayerLife(life, maxLife):
    #DRAW HEALTH
    pygame.draw.rect(Globals.window, COLOR_WHITE, (50,10,100,10), 1)
    life = Clamp(life,0,maxLife)
    if life > 0:
        healthRatio = life / maxLife
        pygame.draw.rect(Globals.window, COLOR_GREEN, (51,11, int(98 * healthRatio), 8))
