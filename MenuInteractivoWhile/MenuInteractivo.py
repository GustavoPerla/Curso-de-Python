#Menu interactivo
print("***** Sistema de administracion de cuentas *****")
op=0
while(op!=3):
    print("""Menu:
        1. Crear cuenta
        2. Eliminar cuenta
        3. Salir""")
    op = int(input("Escoja una opcion: "))
    if op==1:
        print("Creando tu cuenta...\n")
    elif op==2:
        print("Eliminando tu cuenta...\n")
    elif(op==3):
        print("Saliendo del sistema...")
    else:
        print("Numero incorrecto")


