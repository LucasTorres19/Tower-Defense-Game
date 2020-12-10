import pygame as py

class basic_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/bullet.png').convert()
        self.rect = self.sprite.get_rect()
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 10

    def update(self,x,y):

        self.posX = x
        self.posY = y
        
        