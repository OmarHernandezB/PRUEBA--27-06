def menu ():
    menu = """1)Agregar Articulo
2)Listado de Articulos
3)Encontrar Articulo
4)salir""" #definir segun enunciado
    print(menu, end ="")


def opcion_seleccionada():
    while True:
        try:
            opc = int(input())

            if opc>0 or opc<5:
                return opc
            else:
                print("Ingrese una de las opciones")
        except ValueError:
            print("Ingrese una opción númerica")

def agregar ():
    cod = input("Ingrese el código: ")
    nom = input("Ingrese el nombre: ")
    cate = input("Ingrese la categoría: ")
    dire = input("Ingrese el director: ")
    anio = input("Ingrese el año: ")

    res = {"codigo":cod,"nombre":nom,"categoria":cate,"director":dire,"año":anio}
    return res

def lista_Articulo(lista):
    for i in range(len(lista)):
        print(f"Articulo {i+1}:")
        print(f"Código {lista[i]["codigo"]}")
        print(f"Nombre {lista[i]["nombre"]}")
        print(f"Categoría{lista[i]["categoria"]}")
        print(f"Director {lista[i]["director"]}")
        print(f"Año {lista [i]["año"]}")
        print("--------------------------------------------------")

def encontrar_articulo(lista):
    cu = int(input("Ingrese el código del articulo"))
    enc = False

    for i in range(len(lista)):
        if cu == lista[i]["codigo"]:
            res = lista[i]
            encontrado = True

    if encontrado:
        print(f"Articulo {i+1}:")
        print(f"Código {res[i]["codigo"]}")
        print(f"Nombre {res[i]["nombre"]}")
        print(f"Categoría{res[i]["categoria"]}")
        print(f"Director {res[i]["director"]}")
        print(f"Año {res[i]["año"]}")
    else:
        print("Pelicula no encontrada")   
        

def archivo (lista):
    with open("lista_particulos.txt","w") as archivo:
        for i in range (lista):
            res = i["codigo"]+", "+i["nombre"]+", "+i["categoria"]+", "+i["director"]+", "+i["año"]+"\n"
            archivo.write(res)
