#Listas..

print("Listas en Python...")
nombres=["juan","carlos","pepe"]

print(f"Lista de nombres: {nombres}")

print("Lista Heterogenea...")
valores=["pepe",14.2,False,4]
print(f"Lista Heterogenea: {valores}")

#Iterar los elementos de una lista

for nom in nombres:
    print(nom,end="  ")
print()
#Lista de Numeros

numeros=[100,200,300,400]

print(f"Para el indice 0, recuperamos el valor {numeros[0]}")

#Modificar elementos de la lista

numeros[0]=2000
print(f"Para el indice 0, recuperamos el valor {numeros[0]}")

#Preguntar si un valor existe en la lista

num_a_buscar=200
if num_a_buscar in numeros:
    print(f"Existe el numero {num_a_buscar} en mi lista")
else:
    print(f"No existe {num_a_buscar} en la lista")

#Recuperar el indice de cierto elemento

print(f"El indice de {num_a_buscar} es: {numeros.index(num_a_buscar)}")

#Redefinir una lista

num_rec=numeros[0:3]
print(num_rec)

#Metodos de Listas

#Largo de lista

print(f"El largo de la lista numeros es: {len(numeros)}")

#Agregar elemento al final de la lista

numeros.append(500)
print(f"El largo de la lista numeros es: {len(numeros)}")

#Insertar un elemento en cierto indice

numeros.insert(2,50)
print(numeros)

#eliminar un elemento de la lista

numeros.remove(200)

#Concatenar listas

list_concatenada=numeros+valores

#eliminar un elemento por indice

del numeros[3]

#Eliminar lista completa

numeros[:]=[]

#Borar variable por completo

del numeros
