from CONST import *
import Map, Player
from WaveManager import *

def show_fps():
    fps = Clamp(int(clock.get_fps()), 0, 600)
    fpsText = fps_font.render(str(fps), True, COLOR_GREEN)
    Globals.window.blit(fpsText,(0,0))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                NewWave()

        player.handle_event(event)


pygame.init()
Globals.window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)


sky = pygame.image.load(SKY)
sky = pygame.transform.scale(sky, (1000,640))
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

clock =  pygame.time.Clock()

map = Map.Map(Globals.window)
player = Player.Player(Globals.window, map)
Globals.player = player
NewWave()

pygame.display.update()

while True:
    Globals.deltaTime = clock.tick(60)

    #FPS COUNTER
    fps = "FPS : " + str(int(clock.get_fps()))
    pygame.display.set_caption(fps)

    #EVENT
    handle_events()

    #MAP RENDER
    Globals.window.blit(Sky,(-50 - player.x / 8,0))
    map.draw(player.x)
    player.move(map.mapSize)
    player.draw()
    DrawEnnemies()

    #UI RENDER    
    player.inventory.draw()
    DrawWave()

    pygame.display.update()
