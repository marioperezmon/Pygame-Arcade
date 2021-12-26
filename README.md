

# Pygame Arcade

> A set of games developed with pygame

* To add a new game:
  
    ```
    $ vi listaJuegos.py
    (...)
        {
            "nombre": "NombreJuego",
            "lanzador": "/ruta/al/juego/main.py"
        }
    ```

* To create an .exe:
    ```
    $ pyinstaller --onefile -w main.py
    $ dist/main
    ```

### TODO

* corregir e incluir el TresEnRaya
* completar e incluir Snake y Space invaders
* revisar la forma de llamar a los juegos desde el script ppal

