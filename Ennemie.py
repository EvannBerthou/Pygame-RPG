import WaveManager
from CONST import *

class Ennemie: #Base class for all ennemies
    def __init__(self, x,y, core, side):
        self.x = x
        self.y = y
        self.core = core
        self.side = side

    def Walk(self):
        if Distance(self.x, self.core.x, self.y, self.core.y) <= TILE_SIZE * 2:
            WaveManager.Wave.KillEnnemie(self)
            return

        if self.side is "LEFT": #Si l'ennemie a spawn à droite
            self.x += Globals.deltaTime * PlayerSpeed * .5
        elif self.side is "RIGHT":
            self.x -= Globals.deltaTime * PlayerSpeed * .5

    def Draw(self):
        pygame.draw.rect(Globals.window, COLOR_GREEN,(self.x - int(Globals.playerX),self.y, TILE_SIZE, TILE_SIZE))
