from List_Peliculas import List_Peliculas
print("*** App Catalogo de Peliculas ***")

def menu():
    print("""Opciones:
    1. Agregar pelicula
    2. Listar Peliculas
    3. Eliminar catalogo de peliculas
    4. Salir
    """)

op = 0
list = List_Peliculas()
list.leer_peliculas()
while op !=4:
    menu()
    try:
        op=int(input("Escribe tu opcion (1-4): "))

        if 0< op <5:

            if op==1:
                list.agregar_pelicula(input("Proporcione el nombre d ela pelicula: "))
            elif op == 2:
                print(list)
            elif op == 3:
                list.eliminar_catalogo()
            else:
                print("Saliedo del catalogo...")

        else:
            print("Opcion Incorrecta...")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
