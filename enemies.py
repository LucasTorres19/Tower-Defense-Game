import pygame as py
import random

#Clases de los enemigos.

class Cyclops(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Cyclops.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 800
        self.damage = 20
        self.live = True

def create_enemies(x,y):

    enemy = Cyclops(x,y)

    return enemy

#establecer un numero aleatorio de enemigos.

def nro_enemies():

    nro_enemies = random.randint(1,100)    
    
    return nro_enemies 