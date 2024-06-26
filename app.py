import funciones
from os import system

op = 0
peliculas = [] #lista
#codigo,nombre,categoria,director,actores,año

while op !=4:
    system("cls")
    funciones.mostrar_menu()
    op = funciones.get_opcion()

    if op == 1:
        system("cls")
        peliculas.append(funciones.agregar_pelicula())
    elif op == 2:
        system("cls")
        funciones.listar_peliculas(peliculas)
        system("pause")
    elif op == 3:
        system("cls")
        funciones.buscar_pelicula(peliculas)
        system("pause")

funciones.crear_archivo(peliculas)
