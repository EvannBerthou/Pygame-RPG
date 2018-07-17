from CONST import *
import Map, Player

def show_fps():

    fps = Clamp(int(clock.get_fps()), 0, 60)
    fpsText = fps_font.render(str(fps), True, COLOR_GREEN)
    Globals.window.blit(fpsText,(0,0))


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

pygame.display.update()

while True:
    deltaTime = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        player.handle_event(event)

    Globals.window.blit(Sky,(-50 - player.x / 8,0))

    map.draw(player.x)

    player.move(deltaTime, map.mapSize)
    player.draw()
    player.inventory.draw()

    show_fps()

    pygame.display.update()
