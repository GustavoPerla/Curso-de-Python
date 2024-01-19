#Calculadora

print("***** Calculadora en Python *****")
op=0
while op!=5:
    print("""Operaciones que puede realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")
    op=int(input("Escoje una opcion: "))
    if 1 <= op <=4:
        v1 = float(input("Dame el valor 1: "))
        v2 = float(input("Dame el valor 2: "))

    if op==1:
        print(f"El resultado de la suma es: {v1+v2}")
    elif op==2:
        print(f"El resultado de la resta es: {v1 - v2}")
    elif op==3:
        print(f"El resultado de la multiplicacion es: {v1 * v2}")
    elif op==4:
        print(f"El resultado de la division es: {v1 / v2}")
    elif op==5:
        print("Saliendo del programa...")
    else:
        print("Opcion incorrecta...")