from CONST import *
import math, random
from Ennemie import Ennemie
from threading import Thread
from time import sleep

NewWaveTextCountdown = 0

class Wave:
    Ennemies = []
    ENNEMIES_LEFT = 0
    WAVE_COUNT = 0

    def KillEnnemie(ennemie):
        Wave.Ennemies.remove(ennemie)
        Wave.ENNEMIES_LEFT -= 1
        if Wave.ENNEMIES_LEFT is 0:
            NewWave()

class WaveSpawner(Thread):
    def __init__(self, ennmieCount):
        Thread.__init__(self)
        self.ennemieCount = ennmieCount
        self.daemon = False

    def run(self):
        sleep(2)
        for x in range(self.ennemieCount):
            side = "LEFT" if random.randint(0,1) is 0 else "RIGHT"
            x = 0 if side is "LEFT" else Globals.mapX
            Wave.Ennemies.append(Ennemie(x,WINDOW_HEIGHT - 6 * TILE_SIZE, Globals.core,side))
            sleep(random.uniform(0.5,2))    

def DrawWave():
    global NewWaveTextCountdown
    textWave = Wave_font.render("Wave : {}".format(Wave.WAVE_COUNT), True, COLOR_WHITE)
    Globals.window.blit(textWave,(WINDOW_WIDTH - textWave.get_width() - 5,5))
    textEnnemies = Wave_font.render("Ennemies : {}".format(Wave.ENNEMIES_LEFT), True, COLOR_WHITE)
    Globals.window.blit(textEnnemies, (WINDOW_WIDTH - textEnnemies.get_width() - 5, 25))

    if NewWaveTextCountdown > 0:
        DrawNewWaveText()
        NewWaveTextCountdown -= Globals.deltaTime

def NewWave():
    global NewWaveTextCountdown
    NewWaveTextCountdown = 3000
    Wave.Ennemies.clear()
    ENNEMIES_LEFT = 0

    Wave.WAVE_COUNT += 1
    ennemies_count = GetNextWaveCount()

    Globals.core.life = Clamp(Globals.core.life, 0,100)
    Globals.core.life += 25

    spawner = WaveSpawner(ennemies_count)
    spawner.start()

    Wave.ENNEMIES_LEFT = ennemies_count

def GetNextWaveCount():
    return math.ceil(10 * Wave.WAVE_COUNT * 0.75)

def DrawEnnemies():
    for e in Wave.Ennemies:
        e.Draw()
        e.Walk()

def DrawNewWaveText():
    text = NewWave_font.render("New wave incoming !", 0, COLOR_RED)

    surface = pygame.Surface((text.get_width(), text.get_height()))
    surface.blit(text, (0,0,0,0))
    surface.set_colorkey(COLOR_BLACK)
    a = NewWaveTextCountdown / 1500 * 255
    surface.set_alpha(a)

    Globals.window.blit(surface, (WINDOW_WIDTH / 2 - text.get_width() / 2, 25))