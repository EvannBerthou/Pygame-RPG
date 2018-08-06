from CONST import *

class Weapon:
    def __init__(self, maxAmmo, damage, fireRate = 1, auto = False, reloadTime = 1):
        self.maxAmmo = maxAmmo
        self.ammo = maxAmmo
        self.damage = damage
        self.fireRate = fireRate
        self.auto = auto
        self.reloadTime = reloadTime
        self.reloadCooldown = 0
    
    def draw(self): #DRAW AMMO
        string = "{}/{}".format(self.ammo, self.maxAmmo)
        text = Ammo_font.render(string,1, COLOR_WHITE)
        x = WINDOW_WIDTH - text.get_width()
        y = WINDOW_HEIGHT - text.get_height()
        
        Globals.window.blit(text, (x,y,text.get_width(),text.get_height()))
    
    def reload(self):
        self.ammo = self.maxAmmo