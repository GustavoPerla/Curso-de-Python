from Modulo_Funcion import saludar ##tambien se puede poner "*" para importar todas las funciones del archivo

print("*** Manejo de Funciones ***")

#2. llamamos a la funcion

arg =input("Mensaje a enviar: ")
valor = saludar(arg)
print(f"Valor devuelto de la funcion: {valor}")