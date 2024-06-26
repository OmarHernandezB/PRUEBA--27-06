import func

op = 0
peliculas = [] #lista
#codigo,nombre,categoria,director,actores,año

while op !=4:
    func.menu()
    op = func.agregar()

    if op == 1:
        peliculas.append(func.agregar())
    elif op == 2:
        func.lista_Articulo(peliculas)
    elif op == 3:
        func.encontrar_articulo(peliculas)

func.crear_archivo(peliculas)
