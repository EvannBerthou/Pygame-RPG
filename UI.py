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

    def draw(self):
        for x in range(len(self.cases)):
            pygame.draw.rect(Globals.window, COLOR_WHITE, (x * 40 + 25,WINDOW_HEIGHT - 50,34,34), 1)
            if self.cases[x].item is not None:
                pygame.draw.rect(Globals.window, COLOR_GREEN, (x * 40 + 26, WINDOW_HEIGHT - 49,32,32))

    def AddItem(self, item): #Ajoute un item au premier slot libre
        for case in self.cases:
            if case.item is not None:
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
