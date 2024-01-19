#Cajero autoatico ciudad Gotica

print("*** Cajero automatico Ciudad Gotica ***")
op=0
saldo = 0.0
while op!=4:
    print("""Operaciones que puede realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir""")
    op=int(input("Escoje una opcion:"))

    if op==1:
        print(f"El saldo es: ${saldo:.2f}")
    elif op==2:
        ret=float(input("Ingrese la cantidad a retirar: "))
        if ret<=saldo:
            saldo-=ret
            print("El retiro fue exitoso")
        else:
            print(f"Saldo Insuficiente\nEl saldo es: ${saldo:.2f}")
    elif op==3:
        saldo+=float(input("Ingrese la cantidad de dinero a ingresar: "))
    elif op==4:
        print("Saliendo del sistema...")
    else:
        print("Opcion incorrecta...")
