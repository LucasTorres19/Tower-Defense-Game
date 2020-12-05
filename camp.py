import pygame as py

#vars

width = 36
height = 37
margin = 3

def draw_map(SCREEN):
    
    global width 
    global height 
    global margin 
    
    green = (177, 230, 18)

    for fila in range(15):
        for columnas in range(15):
            py.draw.rect(SCREEN,green,[((margin+width) * columnas + margin )+ 170,
                              (margin+height) * fila + margin,
                              width,
                              height])

def place_tower(x,y):
    
    pos_col = y  
    pos_fila = x 

    return pos_fila,pos_col