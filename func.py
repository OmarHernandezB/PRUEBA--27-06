def menu ():
    menu = """1)
    2)
    3)
    3)""" #definir segun enunciado
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

    res = {"Codigo":cod,"Nombre":nom,"Categoria":cod,"Director:":dire,"Año":anio}
    return res

def lista_Articulo(lista):
    for i in range(len(lista_Articulo)):
        print(f"Articulo {i+1}:")
        print(f"Código {lista[i]["Codigo"]}")
        print(f"Nombre {lista[i]["Nombre"]}")
        print(f"Categoría{lista[i]["Categoria"]}")
        print(f"Director {lista[i]["Director"]}")
        print(f"Año {lista [i]["Año"]}")
        print("--------------------------------------------------")

def encontrar_articulo(lista):
    cu = int(input("Ingrese el código del articulo"))
    enc = False

    for i in range(len(lista)):
        if cu == lista[i]["Codigo"]:
            res = lista[i]
            encontrado = True

    if encontrado:
        print(f"Articulo {i+1}:")
        print(f"Código {res[i]["Codigo"]}")
        print(f"Nombre {res[i]["Nombre"]}")
        print(f"Categoría{res[i]["Categoria"]}")
        print(f"Director {res[i]["Director"]}")
        print(f"Año {res[i]["Año"]}")
    else:
        print("Pelicula no encontrada")   
        

def archivo (lista):
    with open("lista_peliculas.txt","w") as archivo:
        for i in range (lista):
            res = i["codigo"]+", "+i["nombre"]+", "+i["categoria"]+", "+i["director"]+", "+i["año"]+"\n"
            archivo.write(res)
