import pygame as py

#Al tocar un boton le asigna el numero a cada torre.
def nro_tower(fila,columna):

    if fila == 0 and columna == 0:
        current_tower = 1
    elif fila == 0 and columna == 1:
        current_tower = 2
    elif fila == 1 and columna == 0:
        current_tower = 3
    elif fila == 1 and columna == 1:
        current_tower = 4
    elif fila == 2 and columna == 0:
        current_tower = 5
    elif fila == 2 and columna == 1:
        current_tower = 6
    elif fila == 3 and columna == 0:
        current_tower = 7
    elif fila == 3 and columna == 1:
        current_tower = 8
    elif fila == 4 and columna == 0:
        current_tower = 9
    elif fila == 4 and columna == 1:
        current_tower = 10
    else:
        current_tower = 0

    return current_tower

#Le da color a los iconos de las torres

def color_icon(fila,columna,array_colors):
    if fila == 0 and columna == 0:
        color = array_colors[0]
    elif fila == 0 and columna == 1:
        color = array_colors[1]
    elif fila == 1 and columna == 0:
        color = array_colors[2]
    elif fila == 1 and columna == 1:
        color = array_colors[3]
    elif fila == 2 and columna == 0:
        color = array_colors[4]
    elif fila == 2 and columna == 1:
        color = array_colors[5]
    elif fila == 3 and columna == 0:
        color = array_colors[6]
    elif fila == 3 and columna == 1:
        color = array_colors[7]
    elif fila == 4 and columna == 0:
        color = array_colors[8]
    elif fila == 4 and columna == 1:
        color = array_colors[9]
    
    return color