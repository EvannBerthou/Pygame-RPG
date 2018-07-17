from CONST import *

def DrawPlayerLife(life, maxLife):
    #DRAW HEALTH
    pygame.draw.rect(Globals.window, COLOR_WHITE, (50,10,100,10), 1)
    life = Clamp(life,0,maxLife)
    healthRatio = life / maxLife
    pygame.draw.rect(Globals.window, COLOR_GREEN, (51,11, int(98 * healthRatio), 8))

class Inventory:
    def __init__(self, size):
        self.cases = []

        for i in range(size):
            self.cases.append(InventoryCase())

        self.ItemsManager = ItemsManager()

    def draw(self):
        for x in range(len(self.cases)):
            pygame.draw.rect(Globals.window, COLOR_WHITE, (x * 40 + 25,WINDOW_HEIGHT - 50,34,34), 1)
            if self.cases[x].item is not None:
                pygame.draw.rect(Globals.window, COLOR_GREEN, (x * 40 + 26, WINDOW_HEIGHT - 49,32,32))

        self.ItemsManager.drawItems()
    def AddItem(self, item): #Ajoute un item au premier slot libre
        for case in self.cases:
            if case.item is None:
                case.SetItem(item)
                return True
        return False

class InventoryCase:
    def __init__(self):
        self.item = None

    def SetItem(self, item):
        if self.item is None:
            self.item = item

    def RemoveItem(self):
        self.item = None

class ItemsManager:
    def __init__(self):
        self.itemsOnMap = []
        self.itemsOnMap.append(Item(10 * TILE_SIZE, 34 * TILE_SIZE, 1))
        self.itemsOnMap.append(Item(30 * TILE_SIZE, 34 * TILE_SIZE, 1))

    def AddItem(self, item):
        self.itemsOnMap.append(item)

    def removeItem(self, item):
        self.itemsOnMap.remove(item)

    def drawItems(self):
        for item in self.itemsOnMap:
            item.draw()

    def CheckCollision(self):
        for item in self.itemsOnMap:
            # print("{} : {} : {}".format(item.x - TILE_SIZE, playerX + 25 * TILE_SIZE, item.x + TILE_SIZE))
            if item.x - TILE_SIZE < Globals.playerX + 25 * TILE_SIZE < item.x + TILE_SIZE: #25 * TILE_SIZE : offset
                self.removeItem(item)
                return item
        return None


class Item:
    def __init__(self, x,y, item):
        self.item = item
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(Globals.window, COLOR_RED, (self.x - int(Globals.playerX), self.y, TILE_SIZE, TILE_SIZE))
