import pygame as py


class basic_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
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
   

def create_tower(nro_tower):

    if nro_tower == 1:
        new_tower = basic_tower()
    elif nro_tower == 2:
        new_tower = toxic_tower()
    elif nro_tower == 3:
        new_tower = basic_tower()
    elif nro_tower == 4:
        new_tower = basic_tower()
    elif nro_tower == 5:
        new_tower = basic_tower()
    elif nro_tower == 6:
        new_tower = basic_tower()
    elif nro_tower == 7:
        new_tower = basic_tower()
    elif nro_tower == 8:
        new_tower = basic_tower()
    elif nro_tower == 9:
        new_tower = basic_tower()
    elif nro_tower == 10:
        new_tower = basic_tower()
            
    return new_tower