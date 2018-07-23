from CONST import *
from Map import *
from UI import *

class Player:

    Player_right = Map.LoadTexture(PLAYER_RIGHT)
    Player_left = Map.LoadTexture(PLAYER_LEFT)

    def TakeDamage(self, damage):
        if self.dead:
            return
        self.health -= damage
        self.DamageTaken = str(damage)
        self.showDamage = True
        self.CountDown = 1 * 1000
        if self.health <= 0:
            print("Dead")
            self.dead = True

    def draw(self):
        DrawPlayerLife(self.health, self.maxHealth)

        #Draw taken damages
        if self.showDamage and not self.dead:
            DamageText = Damage_font.render(self.DamageTaken, True, (255,0,0))
            surface = pygame.Surface(DamageText.get_rect().size, pygame.SRCALPHA)
            surface.blit(DamageText,(0,0))
            Globals.window.blit(surface, (WINDOW_WIDTH / 2,self.y - 25))


        #Draw Player
        if not self.dead:
            x = WINDOW_WIDTH / 2

            sprite = Player.Player_left
            if self.velocity is not 0:
                sprite = Player.Player_right if self.velocity is 1 else Player.Player_left
            else:
                sprite = self.lastSprite

            self.lastSprite = sprite

            Globals.window.blit(sprite,(x,self.y))

            item = self.inventory.ItemsManager.CheckCollision()
            if item is not None:
                self.inventory.AddItem(item)


    def move(self,mapSize):
        if self.dead: #Move only if alive
            return

        self.health += Globals.deltaTime * RegenSpeed
        self.health = Clamp(self.health, 0, self.maxHealth)

        self.CanMoveLeft = not self.map.GetCollsionAt(int(self.x / TILE_SIZE + 25), int(self.y / TILE_SIZE))
        self.CanMoveRight = not self.map.GetCollsionAt(int(self.x / TILE_SIZE + 26), int(self.y / TILE_SIZE))

        if (self.velocity is 1 and self.CanMoveRight) or (self.velocity is -1 and self.CanMoveLeft):
            self.x += self.velocity * PlayerSpeed * Globals.deltaTime

        mapX = (mapSize[0] * TILE_SIZE) - (WINDOW_WIDTH / 2) - TILE_SIZE

        self.x = Clamp(self.x, -400, mapX)
        Globals.playerX = self.x

        if not self.map.GetCollsionAt(int(self.x / TILE_SIZE + 25),int(self.y / TILE_SIZE + 1)):
            self.y += 1

        if self.CountDown > 0:
            self.CountDown -= Globals.deltaTime
        else:
            self.CountDown = 0
            self.showDamage = False

    def handle_event(self,event):
        keys = pygame.key.get_pressed()
        if event.type is pygame.KEYDOWN:
            if self.velocity is 0:
                if keys[KEY_LEFT]:
                    self.velocity = -1
                if keys[KEY_RIGHT]:
                    self.velocity = 1
            if event.key == pygame.K_r:
                self.TakeDamage(50)

        if event.type == pygame.KEYUP:
            if self.velocity is 1 and event.key is KEY_RIGHT:
                self.velocity = 0
            if self.velocity is -1 and event.key is KEY_LEFT:
                self.velocity = 0


    def __init__(self, window, map):
        self.x = 0
        self.y = WINDOW_HEIGHT - 6 * TILE_SIZE
        Globals.window = window
        self.velocity = 0

        self.map = map

        self.maxHealth = 100
        self.health = 0
        self.dead = False

        self.showDamage = False
        self.DamageTaken = ""
        self.CountDown = 0

        self.lastSprite = Player.Player_left

        self.CanMoveLeft = True
        self.CanMoveRight = True

        self.inventory = Inventory(5)

        self.draw()
