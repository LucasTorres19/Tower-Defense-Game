import pygame as py
import bullets 
#Clases de las torres.

class basic_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.nro = 1
        self.sprite = py.image.load('sprites/black.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY = 0
        self.posX = 0 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 120
        self.shooting = False
        self.enemy_shooting = 0
    
    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet

class toxic_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/green.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.shooting = False
        self.range_nro = 120
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet

class ice_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/celeste.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 100
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet 

class water_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/blue.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 200
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet  

class fire_tower(py.sprite.Sprite):
    
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/red.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 200
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet  
       

class poison_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/violet.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 100
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet    
       
class rock_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/brown.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 300
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet   
        

class mud_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/light_brown.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 300
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet   
        

class laser_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/pink.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 500
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet   
        

class bomb_tower(py.sprite.Sprite):

    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.sprite = py.image.load('sprites/dark_green.png').convert()
        self.rect = self.sprite.get_rect()
        self.posY,self.posX = py.mouse.get_pos() 
        self.placed = False
        self.range = (0,0)
        self.range_nro = 200
        self.shooting = False
        self.enemy_shooting = 0

    def create_bullet(self,x,y):

        bullet = bullets.basic_bullet(x,y)

        return bullet

def set_range(x,y,nro_tower):
    
    if nro_tower == 1:
        #basic tower range.
        x = x + 120
        y = y + 120
    elif nro_tower == 2:
        #toxic_tower range.
        x = x + 120
        y = y + 120
    elif nro_tower == 3:
        #ice_tower
        x = x + 100
        y = y + 100
    elif nro_tower == 4:
        #water_tower
        x = x + 200
        y = y + 200
    elif nro_tower == 5:
        #fire_tower
        x = x + 200
        y = y + 200
    elif nro_tower == 6:
        #poison_tower
        x = x + 100
        y = y + 100
    elif nro_tower == 7:
        #rock_tower
        x = x + 300
        y = y + 300
    elif nro_tower == 8:
        #mud_tower
        x = x + 300
        y = y + 300
    elif nro_tower == 9:
        #laser_tower
        x = x + 500
        y = y + 500
    elif nro_tower == 10:
        #bomb_tower
        x = x + 200
        y = y + 200

    return x,y

def set_negative_range(range_number,current_pos):

    if range_number == 100:
        current_pos -= 200
    elif range_number == 120:
        current_pos -= 240
    elif range_number == 200:
        current_pos -= 400
    elif range_number == 300:
        current_pos -= 600
    elif range_number == 500:
        current_pos -= 1000

    return current_pos


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