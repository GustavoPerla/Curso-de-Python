from Funciones import *

print("***** Calculadora en Python con funciones *****")
op=0

while op!=5:
    menu()
    op = float(input("Escoje una opcion: "))
    if op>0 and op<6:
        num1,num2 = ingresarVal()
        if(op==5):
            print("Saliendo de la calculadora...")
        else:
            print(operacion(op,num1,num2))
    else:
        print("Opcion incorrecta")
