print("*** Manejo de exepciones ***")

# try:
#     10/0
#     ##print(mivariable)
# except Exception as e:
#     print(f"Ocurrio un error: {e}")

# try:
#     x=0
#     if x==0:
#         raise Exception("Error la variable x es 0")##Para arrojar exepciones
# except Exception as e:
#     print(f"Ocurrio un error: {e}")

try:
    x=int(input("ingrese un valor entero: "))
    if x==0:
        raise Exception("Error la variable x es 0")##Para arrojar exepciones
except Exception as e:
    print(f"Ocurrio un error: {e}")
else:##Se ejecuta si no hay exepciones
    print("El valor de la variable x es distinto de 0")
finally:#se ejecuta siempre
    print(f"El valor de x validado {x}")