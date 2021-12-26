#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Autor : Mario Perez Montenegro
    Lanza el menu principal del arcade, desde el que se accede a los juegos
'''

def interrupcion(sig, frame):
    salir = input("\n\n[?] CTRL+C detectado... ¿Quieres salir? (S/N)\n").lower()
    
    if salir == "s":
        print("\n[!] Saliendo...\n")
        sys.exit(1)
    else:
        print("\n[!] Continuando...\n")

# Muestra el menu principal y lanza el juego seleccionado
def mainMenu():

    pygame.init()

    txtTitulo = "Pygame Arcade - Menu"
    pygame.display.set_caption(txtTitulo)

    ############################
    # Dimensiones de la pantalla
    ############################
    size = width, height
    screen = pygame.display.set_mode(size)

    screen.fill(col.blanco)

    #######################
    # Dimensiones del titulo
    #######################

    font = pygame.font.Font("OwnFreeSansBold.ttf", 40)
    text = font.render(txtTitulo, True, col.rojo, col.blanco)
    textRect = text.get_rect()
    #textRect.width = 451
    height_titulo = textRect.height # = 42

    ############################
    # Dimensiones de los botones
    ############################

    # TODO comprobar que caben todos los botones necesarios

    # el ancho de los botones depende del juego con nombre mas largo
    width_bt = nombre_mas_largo * 15 + 50
    # posicion a lo ancho donde empiezan los botones
    pos_width_bt = (width / 2) - width_bt/2

    # Hay tantos botones como juegos + 1 (SALIR)
    num_bt = num_juegos + 1

    # tamanho a lo alto de cada boton y separacion a lo alto
    height_bt = separacion_height = 50

    # espacio a lo alto que ocupa el titulo
    espacio_height_titulo = height_titulo + separacion_height

    # espacio a lo alto que ocupan los botones
    espacio_height_bt = num_bt * height_bt + (num_bt-1) * separacion_height

    # espacio a lo alto ocupado en TOTAL
    espacio_height_total = espacio_height_titulo + espacio_height_bt

    # posicion a lo alto donde empieza el titulo
    pos_height_titulo = height/2 - espacio_height_total/2
    textRect.center = (width / 2, pos_height_titulo)

    # posicion a lo alto donde empiezan los botones
    #pos_height_bt = (height / 2) - espacio_total_height_bt/2 + (height_titulo + separacion_height)
    pos_height_bt = pos_height_titulo + espacio_height_titulo

    # lista para almacenar los botones
    botones = []
    i = 0

    # un boton por cada juego
    for juego in lista:
        botones.append(boton(col.rojo, pos_width_bt, pos_height_bt+separacion_height*i, width_bt, height_bt, juego["nombre"], juego["lanzador"]))
        i += 2

    # un boton para salir
    botones.append(boton(col.dorado, pos_width_bt, pos_height_bt+separacion_height*i, width_bt, height_bt, 'SALIR', "quit()"))

    while True:

        screen.fill(col.blanco)

        # Muestra el titulo
        screen.blit(text, textRect)

        for bt in botones:
            bt.draw(screen)

        # sin un for de control de eventos, falla al abrir pygame window
        for event in pygame.event.get():

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                quit()

            # cuando haya un clic
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for bt in botones:
                    if bt.mouseIsOver(mousePos):
                        # TODO -> ver como lanzar el juego a partir de su script lanzador
                        # "Tres en Raya": "from TresEnRaya import tresEnRaya",
                        #print(bt.accion)
                        exec(bt.accion)

            for bt in botones:
                
                # para el boton de SALIR
                if bt.text == "SALIR" and bt.mouseIsOver(mousePos):
                    
                    bt.color = col.doradoClaro
            
                elif bt.text == "SALIR" and not bt.mouseIsOver(mousePos):
                    
                    bt.color = col.dorado
                
                # para el resto de botones
                elif bt.text != "SALIR" and bt.mouseIsOver(mousePos):

                    bt.color = col.rojoClaro

                else:

                    bt.color = col.rojo

        pygame.display.update()


if __name__ == "__main__":

    from somelib import *
    
    #Ctrl + C
    signal.signal(signal.SIGINT, interrupcion)

    # para importar un script para definir variables (colores)
    ''' Una posibilidad es:

    from Resources import *
    print(Colours.rojo)

    Otra posibilidad es:
    '''
    import Resources.Colours as col
    #print("El color rojo es ", col.rojo)

    import listaJuegos
    lista = listaJuegos.lista_juegos
    #print(lista[0]["nombre"])
    
    # para importar una clase (c_boton)
    from Resources.Boton import c_boton as boton
    '''
    pruebaBoton = boton("hola pepe")
    pruebaBoton.test()
    '''

    import pygame

    num_juegos = len(lista)
    nombre_mas_largo = 0
    #juegos_str = ""
    #cont = 1

    for juego in lista:
        '''
        print(str(cont) + " .- " + juego["nombre"] + " - " + juego["lanzador"])
        juegos_str += "\t" + str(cont) + " .- " + juego["nombre"] + " - " + juego["lanzador"] +"\n"
        cont += 1
        '''

        # Busca el nombre del juego mas largo
        if len(juego["nombre"]) > nombre_mas_largo:
            nombre_mas_largo = len(juego["nombre"])

    # Funcion principal (muestra el menu y lanza los juegos)
    mainMenu()

