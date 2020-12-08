import pygame as py

#Clases de las torres.

class basic_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.nro = 1
        self.sprite = py.image.load('sprites/black.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class toxic_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/green.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()
   
class ice_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/celeste.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (50,50)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class water_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/blue.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class fire_tower(py.sprite.Sprite):
    
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/red.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class poison_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/violet.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class rock_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/brown.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class mud_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/light_brown.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class laser_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/pink.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()

class bomb_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/dark_green.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.rangeM = w,h = (100,100)
        self.range = py.Surface(self.rangeM,py.SRCALPHA)
        self.range_rect = self.range.get_rect()


#Funcion para crear los objetos de las torres.

def create_tower(nro_tower):

    if nro_tower == 1:
        new_tower = basic_tower()
    elif nro_tower == 2:
        new_tower = toxic_tower()
    elif nro_tower == 3:
        new_tower = ice_tower()
    elif nro_tower == 4:
        new_tower = water_tower()
    elif nro_tower == 5:
        new_tower = fire_tower()
    elif nro_tower == 6:
        new_tower = poison_tower()
    elif nro_tower == 7:
        new_tower = rock_tower()
    elif nro_tower == 8:
        new_tower = mud_tower()
    elif nro_tower == 9:
        new_tower = laser_tower()
    elif nro_tower == 10:
        new_tower = bomb_tower()
            
    return new_tower