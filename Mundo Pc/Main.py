from Orden import orden

print("Mundo PC\n")

op = 0

orden1 = orden()

def menu():
    print("""Menu de opciones: 
        1. Agregar PC
        2. Ver orden de compras
        3. Salir""")

while op != 3:
    menu()
    op=int(input("Ingrese una opcion: "))
    if 0 < op < 3:
        if op==1:
            orden1.agregar_computadora()
        else:
            print(orden1)
    elif op==3:
        print("Saliendo del programa!!!")
    else:
        print("Opcion incorrecta")