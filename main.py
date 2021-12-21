#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Autor : Mario Perez Montenegro
    Lanza el menu principal del arcade, desde el que se accede a los juegos
'''

if __name__ == "__main__":

    # importa una serie de librerias basicas
    from somelib import *

    # para importar un script para definir variables (colores)
    ''' Una posibilidad seria:

    from Resources import *
    print(Colours.rojo)

    Otra posibilidad seria:
    '''
    import Resources.Colours as col
    '''
    print("El color rojo es", col.rojo)
    '''

    import listaJuegos
    lista = listaJuegos.lista_juegos
    '''
    Se puede acceder con:

    print(lista[1])
    print(lista["nombre"])
    '''
    
    # para importar una clase (c_boton)
    from Resources.Boton import c_boton as boton
    '''
    pruebaBoton = boton("hola pepe")
    pruebaBoton.test()
    '''

    import pygame

    # Bucle principal (muestra el menu y permite acceder a los juegos)

    num_juegos = len(lista)
    print(num_juegos)

    for juego in lista:
        print(".- Juego " + juego["nombre"] + " - " + juego["lanzador"])


    sys.exit(0)



from Boton import boton
from colores import rojo, rojoClaro, azul, negro, blanco, dorado, doradoClaro
import pygame

# Funcion que muestra un menu para elegir el modo de juego
def menuInicial():

    # Inicio configuracion pantalla + juego
    pygame.init()

    # Textos a mostrar en la pantalla inicial
    txtTitulo = "Arcade - Inicio"
    juegos = {}
    juegos[0] = "Tres en Raya"
    juegos[1] = "Snake"

    # Titulo de la ventana
    pygame.display.set_caption(txtTitulo)

    # Tamanho de la pantalla de juego
    size = width, height = 500, 400

    # Configuracion de la pantalla
    screen = pygame.display.set_mode(size)

    # Rellenar la pantalla
    screen.fill(blanco)

    # Botones
    height_bt = (height // 2) - 50 # Separacion de 50 entre botones
    btTresEnRaya = boton(rojo  , 195, height_bt     , 105, 35, juegos[0])
    btSnake = boton(rojo       , 195, height_bt + 50, 105, 35, juegos[1])
    btSalir = boton(dorado     , 215, height_bt + 110, 70, 40, 'SALIR')

    juegoSeleccionado = False

    # Mientras no se haya elegido un juego
    while not juegoSeleccionado:

        # Rellenar la pantalla
        screen.fill(blanco)

        font = pygame.font.Font('freesansbold.ttf', 25)

        # Mostrar TITULO
        text = font.render(txtTitulo, True, rojo, blanco)
        textRect = text.get_rect()
        textRect.center = (width // 2, (height // 2) - 120)
        screen.blit(text, textRect)

        # Muestra los botones
        btTresEnRaya.draw(screen)
        btSnake.draw(screen)
        btSalir.draw(screen)

        # sin un for de control de eventos, falla al abrir pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si se clica en "SALIR"
                if btSalir.mouseIsOver(mousePos):
                    quit()

                # Si se clica en "1 VS 1"
                if btTresEnRaya.mouseIsOver(mousePos):
                    num_juego = 0
                    # print("Modo " + modo[modo_jugar_int] + " seleccionado")
                    return juegos[num_juego]

                # Si se clica en "1 VS PC"
                elif btSnake.mouseIsOver(mousePos):
                    num_juego = 1
                    # print("Modo " + modo[modo_jugar_int] + " seleccionado")
                    return juegos[num_juego]

            if btTresEnRaya.mouseIsOver(mousePos):
                btTresEnRaya.color = rojoClaro
            else:
                btTresEnRaya.color = rojo

            if btSnake.mouseIsOver(mousePos):
                btSnake.color = rojoClaro
            else:
                btSnake.color = rojo

            if btSalir.mouseIsOver(mousePos):
                btSalir.color = doradoClaro
            else:
                btSalir.color = dorado

        pygame.display.update()

# Funcion que lanza el juego elegido
def lanzar_juego(juego):
    listaJuegos = {
        "Tres en Raya": "from TresEnRaya import tresEnRaya",
        "Snake" : "print('Lanzando snake')"
    }

    return (listaJuegos.get(juego, "Error"))

# Funcion que inicia el arcade
def inicio():

    juego = menuInicial()
    # print("El juego seleccionado es " + juego)

    if lanzar_juego(juego) != "Error":
        exec(lanzar_juego(juego))

    else:
        "Error lanzando el juego"

inicio()
