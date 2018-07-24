import WaveManager
from CONST import *

class Ennemie: #Base class for all ennemies
    def __init__(self, x,y, core, side):
        self.x = x
        self.y = y
        self.core = core
        self.side = side
        self.attack = 25
        self.range = TILE_SIZE

    def Walk(self):
        #CHECK COLLISION WITH CORE
        distanceCore = Distance(self.x, self.core.x, 0,0)
        if distanceCore <= TILE_SIZE:
            WaveManager.Wave.KillEnnemie(self)
            return

        #CHECK COLLISION WITH PLAYER
        distancePlayer = Distance(self.x, WINDOW_WIDTH / 2 + Globals.playerX, 0, 0)
        if distancePlayer < self.range:
            Globals.player.TakeDamage(self.attack)


        if self.side is "LEFT": #Si l'ennemie a spawn à droite
            self.x += Globals.deltaTime * PlayerSpeed * .35
        elif self.side is "RIGHT":
            self.x -= Globals.deltaTime * PlayerSpeed * .35

    def Draw(self):
        pygame.draw.rect(Globals.window, COLOR_GREEN,(self.x - int(Globals.playerX),self.y, TILE_SIZE, TILE_SIZE))
