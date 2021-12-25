

# Pygame Arcade

> A set of games developed with pygame

* Para incluir rapidamente nuevos juegos:
  
    ```
    $ vi listaJuegos.py
    (...)
        {
            "nombre": "NombreJuego",
            "lanzador": "/ruta/de/ejemplo/Juego/main.py"
        }
    ```
  
* Para generar un ejecutable:
    ```
    $ pyinstaller --onefile -w main.py
    $ dist/main
    ```

### TODO

* corregir e incluir el TresEnRaya
* completar e incluir Snake y Space invaders
* revisar la forma de llamar a los juegos desde el script ppal

