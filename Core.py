from CONST import *

class Core:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 100

    def DrawLife(self):
        self.life = Clamp(self.life, 0,100)
        x = self.x - int(Globals.playerX) - TILE_SIZE
        y = self.y - TILE_SIZE

        outlineRect = (x, y, 50,8)
        pygame.draw.rect(Globals.window, COLOR_WHITE, outlineRect, 1)
        
        if self.life > 0:
            healthRatio = Clamp(int(48 * (self.life / 100)),0,100)
            inlineRect = (x + 1, y + 1, healthRatio ,6)
            pygame.draw.rect(Globals.window, COLOR_GREEN, inlineRect)