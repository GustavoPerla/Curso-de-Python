from Funciones import *

prod =[
    {"id":0,"nombre":"Papas","precio":300},
    {"id":1,"nombre":"Refresco","precio":50},
    {"id":2,"nombre":"Sandwich","precio":120}
]

print("*** Maquina de snacks ***")
op=0

mostrarProd(prod)
compra = []
while op!=3:
    print(f"""Menu:
    1. Comprar snack
    2. Mostrar ticket
    3. Salir""")
    op=int(input("Escoge una opcion: "))

    if op==1:
        snack=int(input("Que snack quieres (Id): "))
        if snack>=0 and snack<len(prod):
            print(f"Ok, snack agregado{prod[snack]}")
            compra.append(prod[snack])
        else:
            print("Opcion incorrecta...")
    elif op==2:
        mostrarTicket(compra)
    elif op==3:
        print("Regresa pronto!")
    else:
        print("Opcion incorrecta")
