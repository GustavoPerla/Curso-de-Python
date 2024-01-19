def menu():
    print("""Operaciones que puedes realizar:
    \t1. Suma
    \t2. Resta
    \t3. Multiplicacion
    \t4. Division
    \t5. Salir""")

def ingresarVal():
    val1=float(input("Dame el valor 1: "))
    val2=float(input("Dame el valor 1: "))
    return val1, val2

def operacion(op, num1, num2):
    if op==1:
        return f"El resultado de la suma es: {num1+num2}"
    elif op == 2:
        return f"El resultado de la resta es: {num1-num2}"
    elif op == 3:
        return f"El resultado de la multiplicacion es: {num1*num2}"
    else:
        return f"El resultado de la division es: {num1/num2 if num2!=0 else "No se puede dividir por 0"}"  ## if corto en python