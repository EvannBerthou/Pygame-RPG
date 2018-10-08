from CONST import *
from Weapon import *

class Inventory:
    def __init__(self, size):
        self.cases = []

        for i in range(size):
            self.cases.append(InventoryCase())

        self.ItemsManager = ItemsManager()
        self.active = 0

    def draw(self):
        for x in range(len(self.cases)):
            outline_color = COLOR_RED if self.active is x and self.cases[0].item is not None else COLOR_WHITE
            pygame.draw.rect(Globals.window, outline_color, (x * 40 + 25,WINDOW_HEIGHT - 50,34,34), 1)
            if self.cases[x].item is not None:
                pygame.draw.rect(Globals.window, COLOR_GREEN, (x * 40 + 26, WINDOW_HEIGHT - 49,32,32))

        self.ItemsManager.drawItems()

    def AddItem(self, item): #Ajoute un item au premier slot libre
        for case in self.cases:
            if case.item is None:
                case.SetItem(item.item)
                Globals.player.ActiveWeapon = item.item
                return True
        return False

    def GetItem(self, key, currentActive):
        #OTPIMIZE
        if key is "&" and self.cases[0] is not None:
            self.active = 0
            return self.cases[0].item
        if key is "é" and self.cases[1] is not None:
            self.active = 1
            return self.cases[1].item
        if key is '"' and self.cases[2] is not None:
            self.active = 2
            return self.cases[2].item
        if key is "'" and self.cases[3] is not None:
            self.active = 3
            return self.cases[3].item
        if key is "(" and self.cases[4] is not None:
            self.active = 4
            return self.cases[4].item

        return currentActive

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
        self.itemsOnMap.append(Item(10 * TILE_SIZE, 34 * TILE_SIZE, Weapon(30,25)))
        self.itemsOnMap.append(Item(30 * TILE_SIZE, 34 * TILE_SIZE, Weapon(20,100)))

    def AddItem(self, item):
        self.itemsOnMap.append(item)

    def removeItem(self, item):
        self.itemsOnMap.remove(item)

    def drawItems(self):
        for item in self.itemsOnMap:
            item.draw()

    def CheckCollision(self):
        for item in self.itemsOnMap:
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
