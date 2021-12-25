#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Autor : Mario Perez Montenegro
    Lanza el menu principal del arcade, desde el que se accede a los juegos
'''

# Muestra el menu principal y devuelve la posicion del juego seleccionado
def mainMenu():

    pygame.init()

    font = pygame.font.Font('freesansbold.ttf', 25)

    # Titulo
    txtTitulo = "Pygame Arcade - Menu"
    pygame.display.set_caption(txtTitulo)

    # Dimensiones
    size = width, height
    screen = pygame.display.set_mode(size)

    screen.fill(col.blanco)

    # Hay tantos botones como juegos + 1 (SALIR)
    num_bt = num_juegos + 1

    # el ancho de los botones depende del juego con nombre mas largo
    width_bt = nombre_mas_largo * 8 + 40
    # ancho donde empiezan los botones
    pos_width_bt = (width / 2) - width_bt/2

    height_bt = separacion_height_bt = 35
    espacio_total_height_bt = num_bt * (height_bt + separacion_height_bt) - separacion_height_bt # el ultimo boton no tiene separacion por debajo
    # alto donde empiezan los botones
    pos_height_bt = (height / 2) - espacio_total_height_bt/2

    # TODO -> adaptar la creacion de botones para que se ajuste "dinamicamente" al añadir juegos a la lista
    
    bt_0 = boton(col.rojo     , pos_width_bt, pos_height_bt                     , width_bt, height_bt, lista[0]["nombre"])
    bt_1 = boton(col.rojo     , pos_width_bt, pos_height_bt+separacion_height_bt*2, width_bt, height_bt, lista[1]["nombre"])
    
    btSalir = boton(col.dorado, pos_width_bt, pos_height_bt+separacion_height_bt*4, width_bt, height_bt, 'SALIR')

    while True:

        screen.fill(col.blanco)

        # Muestra el titulo y los botones
        '''
        text = font.render(txtTitulo, True, col.rojo, col.blanco)
        textRect = text.get_rect()
        textRect.center = (width // 2, (height // 2) - 120)
        screen.blit(text, textRect)
        '''

        bt_0.draw(screen)
        bt_1.draw(screen)
        btSalir.draw(screen)

        # sin un for de control de eventos, falla al abrir pygame window
        for event in pygame.event.get():

            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                quit()

            # cuando haya un clic
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Click en "SALIR"
                if btSalir.mouseIsOver(mousePos):
                    quit()

                # Click en "Tres En Raya"
                if bt_0.mouseIsOver(mousePos):
                    print("Juego Tres en raya seleccionado")
                    return 0

                # Click en "Snake"
                elif bt_1.mouseIsOver(mousePos):
                    print("Juego Snake seleccionado")
                    return 1

            if bt_0.mouseIsOver(mousePos):
                bt_0.color = col.rojoClaro
            else:
                bt_0.color = col.rojo

            if bt_1.mouseIsOver(mousePos):
                bt_1.color = col.rojoClaro
            else:
                bt_1.color = col.rojo

            if btSalir.mouseIsOver(mousePos):
                btSalir.color = col.doradoClaro
            else:
                btSalir.color = col.dorado

        pygame.display.update()

    '''
    menu = "\n [!] Bienvenido al menu principal! Juegos disponibles:\n" + juegos_str + "\n" + \
        " [!] Opciones:\n" + \
        "\t[1 - " + str(num_juegos) + "] Iniciar juego\n" + \
        "\t[0] Salir\n"

    while True:

        print(menu)

        op = int(input("Opcion elegida? "))

        if op == 0:
            print("\nOK, saliendo...\n")
            sys.exit(0)
        else:
            # la opcion 1 es la posicion 0 de la lista de juegos y sucesivamente...
            op -= 1
            nombre_juego = lista[op]["nombre"]
            print("\nLanzando el juego " + nombre_juego)
            time.sleep(3)
            print("Fin del " + nombre_juego + "...")
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
    print(lista[0]["nombre"])
    '''
    
    # para importar una clase (c_boton)
    from Resources.Boton import c_boton as boton
    '''
    pruebaBoton = boton("hola pepe")
    pruebaBoton.test()
    '''

    import pygame

    cont = 1
    juegos_str = ""
    num_juegos = len(lista)
    nombre_mas_largo = 0

    for juego in lista:
        #print(str(cont) + " .- " + juego["nombre"] + " - " + juego["lanzador"])
        juegos_str += "\t" + str(cont) + " .- " + juego["nombre"] + " - " + juego["lanzador"] +"\n"
        cont += 1

        #print(juego["nombre"], len(juego["nombre"]))

        # Busca el nombre del juego mas largo
        if len(juego["nombre"]) > nombre_mas_largo:
            nombre_mas_largo = len(juego["nombre"])

    # Funcion principal (muestra el menu y permite acceder a los juegos)
    pos_juego = mainMenu()

    print("Hay que lanzar el juego " + str(lista[pos_juego]["nombre"]))
    print("exec(" + lista[pos_juego]["lanzador"] + ")")
    exec(lista[pos_juego]["lanzador"])

    # "Tres en Raya": "from TresEnRaya import tresEnRaya",

