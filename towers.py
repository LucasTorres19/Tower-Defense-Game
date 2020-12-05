import pygame as py

class Tower_Basic(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/black.png')
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False


def create_tower(nro_tower):

    if nro_tower == 1:
        new_tower = Tower_Basic()
    elif nro_tower == 2:
        new_tower = Tower_Basic()
    elif nro_tower == 3:
        new_tower = Tower_Basic()
    elif nro_tower == 4:
        new_tower = Tower_Basic()
    elif nro_tower == 5:
        new_tower = Tower_Basic()
    elif nro_tower == 6:
        new_tower = Tower_Basic()
    elif nro_tower == 7:
        new_tower = Tower_Basic()
    elif nro_tower == 8:
        new_tower = Tower_Basic()
    elif nro_tower == 9:
        new_tower = Tower_Basic()
    elif nro_tower == 10:
        new_tower = Tower_Basic()
            
    return new_tower