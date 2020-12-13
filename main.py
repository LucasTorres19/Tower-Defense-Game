#librerias
import pygame as py
import sys
#archivos
import menu_tower as mt
import camp as m
import towers as t
import enemies as en
import random

py.init()

#const y variables.

WIDTH = 800
HEIGHT = 600
SCREEN = py.display.set_mode((WIDTH,HEIGHT))
CLOCK = py.time.Clock()

#Grid de towers

grid = []
LARGO = 44
ALTO = 44
MARGIN = 5

#iconos de las torres.

grid_icon = []
icon_largo = 36
icon_alto = 37
icon_margin = 11

#enemigos
enemies = []
nro_enemies = 0
create_enemies = False
enemies_dead = 0
bullets = []


#towers
current_tower = 0
tower_array = []
have_tower = False

#Colors.

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = ( 0, 255, 0)
RED = (255,0,0)
GREY = (225, 237, 228)
towers_colors = [(0,0,0),(0,255,0),(0,255,255),(0,0,255),(255,0,0),(40,25,55),(23,23,10),(100,100,0),(100,21,100),(1,40,2)]
#Config

py.display.set_caption('Insertar nombre aqui.')

#menu de torres 
def Crear_grid():
    global grid
    global grid_icon

    for fila in range(5):
        grid.append([])
        for columna in range(2):
            grid[fila].append(0)

    for fila1 in range(5):
        grid_icon.append([])
        for columna2 in range(2):
            grid_icon[fila1].append(0)        

#menu de torres.
def Dibujar_grid():

    global grid
    global grid_icon
    global towers_colors

    for fila1 in  range(5):
        for columna2 in range(2):
            color = WHITE
            if grid[fila1][columna2] == 1:
                color = RED
            elif grid[fila1][columna2] == 0:
                color = WHITE   
            py.draw.rect(SCREEN,color,[((MARGIN+LARGO) * columna2 + MARGIN),
                              (MARGIN+ALTO) * fila1 + MARGIN,
                              LARGO,
                              ALTO])

        for fila2 in  range(5):
            for columna3 in range(2):
                color = mt.color_icon(fila2,columna3,towers_colors)  
                py.draw.rect(SCREEN,color,[((icon_margin+icon_largo) * columna3 + icon_margin),
                                (icon_margin+icon_alto) * fila2 + icon_margin,
                                icon_largo,
                                icon_alto])

def main():
    
    #globales

    global grid
    global current_tower
    global towers_colors
    global tower_array
    global have_tower
    global enemies
    global bullets
    global nro_enemies
    global create_enemies
    global enemies_dead

    #grid de torres.
    Crear_grid()
         
    running = True
    while running:

      
        SCREEN.fill(BLACK)

        #verificador de eventos.
        for event in py.event.get():

            if event.type == py.QUIT:
                running = False
                sys.exit()
            
            elif event.type == py.MOUSEBUTTONDOWN:
                
                mouse_pos = py.mouse.get_pos()
                pos_com = mouse_pos[0] // (LARGO + MARGIN)
                pos_fila = mouse_pos[1] // (ALTO + MARGIN)

                #Verificar que este dentro del menu de torres y si no tenes ya una torre selecionada.
                if pos_com in range(0,2) and pos_fila in range(0,5) and have_tower == False:
                    grid[pos_fila][pos_com] = 1
                    current_tower = mt.nro_tower(pos_fila,pos_com)

                    #borrar 1 que pueda haber en otro campo.
                    for fila in range(5):
                        for columna in range(2):
                            if fila == pos_fila and columna == pos_com:
                                grid[fila][columna] = 1
                            else:
                                grid[fila][columna] = 0

                    #Agregar la torre al array de torres
                    for i in range(0,len(tower_array)+1):
                        if i == len(tower_array):
                            tower_array.append(t.create_tower(current_tower))                
                            have_tower = True
                
                #Si la torre todavia no fue colocada , tomar la posicion del mouse y ponerla.
                if have_tower == True:
                    if tower_array[len(tower_array)-1].placed == False:
                        if mouse_pos[0] in range(173,756):
                            tower_array[i].posX,tower_array[i].posY = py.mouse.get_pos() 
                            tower_array[i].range = (t.set_range(tower_array[i].posX,tower_array[i].posY,current_tower))
                            tower_array[i].placed = True
                            have_tower = False
                
        m.draw_map(SCREEN)
        Dibujar_grid()
        
        #-------------------------------------------------------------
        #Hay que arreglar la generacion automatica de enemigos.
        #-------------------------------------------------------------
        
        print(len(enemies))
        #creacion de enemigos.
        if  nro_enemies == enemies_dead:
            nro_enemies = en.nro_enemies()
            enemies_dead = 0
            
            while enemies != []:
                enemies.clear()

            for o in range(0,nro_enemies):
                if o == len(enemies):
                    enemies.append(en.create_enemies(random.randint(200,500),200)) 
        
            
        #verficacion de colisiones y calculos de daño.

        #arreglar que las torres solo disparen a un objetivo.
        
        for h in range(len(tower_array)):
            
            for g in range(len(enemies)):
                #Verificar si la torres ya le esta disparando a un enemigo.
                if tower_array[h].shooting == True:

                     enemies[tower_array[h].enemy_shooting].hp -= bullet.damage
                     tower_array[h].shooting = True

                     if enemies[tower_array[h].enemy_shooting].hp <= 0:  
                            enemies[tower_array[h].enemy_shooting].kill()
                            enemies[tower_array[h].enemy_shooting].live = False
                            tower_array[h].shooting = False
                            enemies_dead += 1
            
                            
                
                #Verificar si un enemigo esta dentro del rango de la torre.
                elif enemies[g].posX in range(t.set_negative_range(tower_array[h].range_nro,tower_array[h].range[0]),tower_array[h].range[0]) and enemies[g].posY in range(t.set_negative_range(tower_array[h].range_nro,tower_array[h].range[1]),tower_array[h].range[1]):
                    
                    #creando la bala
                    bullet = tower_array[h].create_bullet(tower_array[h].posX,tower_array[h].posY)
                    
                    bullet.update(enemies[g].posX,enemies[g].posY)
                    
                    #verificando colision.
                    if py.sprite.collide_rect(bullet, enemies[g]) and enemies[g].live == True:

                        #calculando daño.
                        enemies[g].hp -= bullet.damage
                        tower_array[h].shooting = True
                        tower_array[h].enemy_shooting = g
                        if enemies[g].hp <= 0:  
                            enemies[g].kill()
                            enemies[g].live = False
                            tower_array[h].shooting = False
                            enemies_dead += 1
            
        #movimiento de los enemigos y dibujo

        for p in range(len(enemies)):
            if enemies[p].live == True:
               enemies[p].posY += 0.5
          

        #Verificando que los enemigos siguen vivos para dibujarlos. 
        for y in range(len(enemies)):
            if enemies[y].live == True:
                SCREEN.blit(enemies[y].sprite,(enemies[y].posX,enemies[y].posY))
                
                #verificar si existe alguna bala.
                try:
                    SCREEN.blit(bullet.sprite,(bullet.posX,bullet.posY))
                except:
                    error = True

        #Dibujando las torres.
        for i in range(len(tower_array)):
            if tower_array[i].placed == False:                
                SCREEN.blit(tower_array[i].sprite,py.mouse.get_pos())
            else:
                #Torre
                SCREEN.blit(tower_array[i].sprite,m.place_tower(tower_array[i].posX,tower_array[i].posY))
                tower_array[i].placed == True
        
        CLOCK.tick(30)
        py.display.flip()

if __name__ == "__main__":
    main()