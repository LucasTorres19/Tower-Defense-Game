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
        self.hp = 400
        self.damage = 20
        self.live = True
        self.speed = 0.5

class Dark_enemy(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/dark_enemy.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 500
        self.damage = 20
        self.live = True
        self.speed = 0.5

class Orc(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Orn.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 5000
        self.damage = 20
        self.live = True
        self.speed = 0.5

class Sleepyhead(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/sleepyhead.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 700
        self.damage = 20
        self.live = True
        self.speed = 0.5

class Ogre(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/ogre.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 7000
        self.damage = 20
        self.live = True
        self.speed = 0.5

class Sick(py.sprite.Sprite):
    
    def __init__(self,x ,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/sick.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.hp = 500
        self.damage = 20
        self.live = True
        self.speed = 0.5

def create_enemies(x,y):

    #apartir de un numero random crear un enemigo diferente.

    nro = random.randint(1,3)
    var = random.randint(1,2)

    if nro == 1 and var == 1:
        enemy = Cyclops(x,y)
    elif nro == 1 and var == 2:
        enemy = Sleepyhead(x,y)
    elif nro == 2 and var == 1:
        enemy = Dark_enemy(x,y)
    elif nro == 2 and var == 2:
        enemy = Sick(x,y)
    elif nro == 3 and var == 1:
        enemy = Orc(x,y)
    elif nro == 3 and var == 2:
        enemy = Ogre(x,y)
    return enemy

#establecer un numero aleatorio de enemigos.

def nro_enemies():

    nro_enemies = random.randint(20,100)    
    
    return nro_enemies 