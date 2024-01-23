import os ## libreria del SO para borrar archivos y demas

#Crear un archivo vacio

nom_arch = "mi_archivo.txt"

##archivo = open(nom_arch,"x")## x es para crear archivos
#print(f"Se creo el archivo: {nom_arch}")


#Escribir un archivo
# print("Escribir un archivo")
# archivo = open(nom_arch,"w") Tambien se puede utilizar w+ para crear, sobreescribir y leer un archivo
# archivo.write("Hola mundo\n")
# archivo.close()

#Anexar archivo // escribir al final del archivo sin borrar nada

# print("Anexando informacion al archivo:")
# archivo = open(nom_arch,"a")  Tambien se puede utilizar a+ para crear, escribir al final del archivo y leer un archivo
# archivo.write("Anexando informacion\n")
# archivo.close()
#
# #Leer un archivo
#
# print("Leer de un archivo:")
# archivo = open(nom_arch,"r")  Tambien se puede utilizar r+ para sobreescribir y leer un archivo
# print(archivo.read()) ## tambien esta el metodo readlines para leer toda un linea
# archivo.close()

#Leer lineas de un archivo

archivo = open(nom_arch) ## por default se abre en modo lectura
for linea in archivo:
    print(linea)
archivo.close()

##leo una lista

archivo = open(nom_arch)
lineas = archivo.readlines()
for linea in lineas:
    print(linea)
archivo.close()

#Abrir el archivo como recurso para que se cierre automaticamente

with open(nom_arch) as archivo:
    print(archivo.read())

if(os.path.exists(nom_arch)):
    os.remove(nom_arch) ## borrar archivo
    print(f"Se elimino el archivo {nom_arch}")
else:
    print(f"Archivo {nom_arch} no encontrado")