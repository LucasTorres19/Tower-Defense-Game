import pygame as py

class Tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/black.png')
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False


def create_tower(nro_tower):

    if nro_tower == 1:
        new_tower = Tower()
    
    return new_tower