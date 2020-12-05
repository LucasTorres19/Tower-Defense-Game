import pygame as py


def draw_map(SCREEN):
    
    width = 36
    height = 37
    margin = 3
    green = (177, 230, 18)

    for fila in range(15):
        for columnas in range(15):
            py.draw.rect(SCREEN,green,[((margin+width) * columnas + margin )+ 170,
                              (margin+height) * fila + margin,
                              width,
                              height])


