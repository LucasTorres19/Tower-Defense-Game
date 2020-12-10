import pygame as py

#vars

width = 36
height = 37
margin = 3

def draw_map(SCREEN):
    
    global width 
    global height 
    global margin 
    
    color1= (250, 167, 72)
    color2= (250, 215, 175)

    for fila in range(15):
        for columnas in range(15):
            if columnas % 2 == 0:
                py.draw.rect(SCREEN,color1,[((margin+width) * columnas + margin )+ 170,
                                (margin+height) * fila + margin,
                                width,
                                height])
            elif fila % 2 == 0:
                py.draw.rect(SCREEN,color1,[((margin+width) * columnas + margin )+ 170,
                                (margin+height) * fila + margin,
                                width,
                                height])
            else:
                 py.draw.rect(SCREEN,color2,[((margin+width) * columnas + margin )+ 170,
                                (margin+height) * fila + margin,
                                width,
                                height])

def place_tower(x,y):
    
    pos_col = y  
    pos_fila = x 

    return pos_fila,pos_col