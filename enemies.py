import pygame as py


#Clases de los enemigos.

class Cyclops(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Cyclops.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 20
        self.damage = 20
        self.live = True

def create_enemies(x,y):

    enemy = Cyclops(x,y)

    return enemy