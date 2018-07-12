import pygame
from pygame.locals import *
from CONST import *
import Map, Player

def show_fps():
    fps = int(clock.get_fps())
    fpsText = fps_font.render(str(fps), True, COLOR_GREEN)
    window.blit(fpsText,(0,0))


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)

sky = pygame.image.load(SKY)
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

clock =  pygame.time.Clock()
fps_font = pygame.font.SysFont("Arial", 20)

map = Map.Map(window)
player = Player.Player(window)

pygame.display.update()

while True:
    deltaTime = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        player.handle_event(event)

    window.fill(COLOR_BLACK)

    window.blit(Sky,(-50 - player.x / 8,0))

    map.draw(player.x, 0)

    player.move(deltaTime, map.mapSize)
    player.draw()

    show_fps()

    pygame.display.update()
