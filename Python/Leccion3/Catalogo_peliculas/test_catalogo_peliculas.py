from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('Catalogo de peliculas')
        print('Opciones: ')
        print('1. Agregar Peli')
        print('2. Lista de pelis')
        print('3. Eliminar catalogo de pelis')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4):'))
        if opcion ==1:
            nombre_peli = input('Digite el nombre de la peli: ')
            pelicula= Pelicula(nombre_peli)
            cp.agregar_peliculas(pelicula)
        elif opcion ==2:
            cp.listar_peliculas()
        elif opcion ==3:
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Saliendo del programa.....')
