from Funciones import *

prod = Snacks()

print("*** Maquina de snacks ***")
op=0

mostrarProd(prod)
compra = []
while op!=5:
    menu()
    op=int(input("Escoge una opcion: "))

    if op==1:
        snack=int(input("Que snack quieres (Id): "))
        if snack>0 and snack<=len(prod.obtener_list()):
            print(f"Ok, snack agregado {Obtener_prod(snack)}")
            compra.append(Obtener_prod(snack))
        else:
            print("Opcion incorrecta...")
    elif op==2:
        mostrarTicket(compra)
    elif op == 3:
        prod.agregar_snack(input("Ingrese el nombre del Snack: "),float(input("Ingrese el precio del snack: ")))
    elif op == 4:
        mostrarProd(prod)
    elif op==5:
        print("Regresa pronto!")
    else:
        print("Opcion incorrecta")
