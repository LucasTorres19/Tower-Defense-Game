import pygame as py

class basic_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/bullet.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "normal"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 10

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Toxic_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Toxic_Bullet.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Toxic"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 20

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Ice_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/ice_Bullet.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "ice"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 20

    def update(self,x,y):

        self.posX = x
        self.posY = y


class Water_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Water.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Water"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 10

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Fire_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Fire.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Fire"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 40

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Poison_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Toxic_Bullet.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Poison"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 30

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Rock_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Rock.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Rock"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 50

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Mud_bullet(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/Mud.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "mud"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 20

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Laser(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/laser.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "laser"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 70

    def update(self,x,y):

        self.posX = x
        self.posY = y

class Bomb(py.sprite.Sprite):

    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/BOMB.png').convert()
        self.rect = self.sprite.get_rect()
        self.type = "Bomb"
        self.posX = x
        self.posY = y
        self.vel = 3
        self.damage = 100

    def update(self,x,y):

        self.posX = x
        self.posY = y

def disadvantage(bullet_type,enemy):

    if bullet_type == "Basic":
        return
    elif bullet_type == "Toxic":
        enemy.hp -= 2
    elif bullet_type == "Ice":
        enemy.posY -= 50
        enemy.speed = 0.4
    elif bullet_type == "Water":
        enemy.posY -= 70
    elif bullet_type == "Fire":
        enemy.hp -= 100
    elif bullet_type == "poison":
        enemy.hp -= 50
        enemy.posX -= 100
        enemy.posY -= 100
    elif bullet_type == "Rock":
        enemy.posX -= 200
    elif bullet_type == "mud":
        enemy.speed = 0.1
    elif bullet_type == "laser":
       return
    elif bullet_type == "Bomb":
       return
    