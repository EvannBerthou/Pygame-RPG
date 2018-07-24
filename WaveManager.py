from CONST import *
import math, random
from Ennemie import Ennemie
from threading import Thread
from time import sleep


class Wave:
    Ennemies = []
    ENNEMIES_LEFT = 0
    WAVE_COUNT = 0

    def KillEnnemie(ennemie):
        Wave.Ennemies.remove(ennemie)
        Wave.ENNEMIES_LEFT -= 1
        Globals.core.life -= ennemie.attack
        if Wave.ENNEMIES_LEFT is 0:
            NewWave()

class WaveSpawner(Thread):
    def __init__(self, ennmieCount):
        Thread.__init__(self)
        self.ennemieCount = ennmieCount
    
    def run(self):
        for x in range(self.ennemieCount):
            side = "LEFT" if random.randint(0,1) is 0 else "RIGHT"
            x = 0 if side is "LEFT" else Globals.mapX
            Wave.Ennemies.append(Ennemie(x,WINDOW_HEIGHT - 6 * TILE_SIZE, Globals.core,side))
            sleep(random.uniform(0.5,2))    

def DrawWave():
    textWave = Wave_font.render("Wave : {}".format(Wave.WAVE_COUNT), True, COLOR_WHITE)
    Globals.window.blit(textWave,(WINDOW_WIDTH - textWave.get_width() - 5,5))
    textEnnemies = Wave_font.render("Ennmies : {}".format(Wave.ENNEMIES_LEFT), True, COLOR_WHITE)
    Globals.window.blit(textEnnemies, (WINDOW_WIDTH - textEnnemies.get_width() - 5, 25))

def NewWave():
    Wave.Ennemies.clear()
    ENNEMIES_LEFT = 0

    Wave.WAVE_COUNT += 1
    ennemies_count = GetNextWaveCount()

    spawner = WaveSpawner(ennemies_count)
    spawner.start()

    Wave.ENNEMIES_LEFT = ennemies_count

def GetNextWaveCount():
    return math.ceil(10 * Wave.WAVE_COUNT * 0.75)

def DrawEnnemies():
    for e in Wave.Ennemies:
        e.Draw()
        e.Walk()
