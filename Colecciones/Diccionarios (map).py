#Manejo de diccionarios
#almacena sus elementos en forma de llave : valor
#y ademas no se pueden duplicar sus elementos
dicc = {"nombre":"Rodrigo","apellido":"Cervantes","edad":28}

##Acceder a los elementos

print(f"Nombre: {dicc['nombre']}")
print(f'Edad: {dicc.get("edad")}')

#Agregar un nuevo elemento

dicc["tel"]=1312131212
print(dicc)

#Obtener una lista de las llaves del diccionario

print(f"lista de llaves del diccionario: {dicc.keys()}")

#Obtener una lista de los valores del diccionario

print(f"Lista de valores del diccionario: {dicc.values()}")

##Obtener los elementos del dicccionario(items: clave valor)

print(f"Lista de los elementos del diccionario: {dicc.items()}")

#Revisar si existe una llave ene le diccionario

clave="nombre"
if clave in dicc:
    print(f"La llave {clave} existe en el diccionario")
else:
    print(f"La llave {clave} no existe en el diccionario")

#Actualizar un elemento del diccionario

dicc["edad"]=89

#Eliminar un elemento del diccionario

dicc.pop("tel")

#Recorrer los elementos como una tupla

for clave, valor in dicc.items():
    print(f"{clave} : {valor}",end="    ")
print()

#Eliminar todo el diccionario

dicc.clear()