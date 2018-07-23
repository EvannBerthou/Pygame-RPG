from CONST import *
import math
from Ennemie import Ennemie


class Wave:
    Ennemies = []
    ENNEMIES_LEFT = 0
    WAVE_COUNT = 0

    def KillEnnemie(ennemie):
        Wave.Ennemies.remove(ennemie)
        Wave.ENNEMIES_LEFT -= 1
        if Wave.ENNEMIES_LEFT is 0:
            NewWave()

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

    ## TODO: ADD DELAY BETWEEN SPAWNS
    for x in range(ennemies_count):
        Wave.Ennemies.append(Ennemie(0,WINDOW_HEIGHT - 6 * TILE_SIZE, Globals.core,"LEFT"))

    Wave.ENNEMIES_LEFT = ennemies_count

def GetNextWaveCount():
    return math.ceil(10 * Wave.WAVE_COUNT * 0.75)

def DrawEnnemies():
    for e in Wave.Ennemies:
        e.Draw()
        e.Walk()

def Kill(ennemie):
    print("test")
    Wave.Ennemies.remove(ennemie)
    Wave.ENNEMIES_LEFT -= 1
