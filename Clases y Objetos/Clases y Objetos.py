from Clases import *

print("*** Clases y objetos en Python ***")

contacto1 = Contacto()

contacto1.definirAtri("Juan","Perez",1124096375,"Juanperez@gmail.com")
contacto1.mostrarAtri()
##Motrar direccion de memoria de un objeto
print(f"Direccion de memoria de contacto1 : {id(contacto1)}")
print(f"Direccion de memoria de contacto1 en hexa : {hex(id(contacto1))}")

contacto2 = Contacto()
contacto2.definirAtri("Carlos","Gomez",55789898,"cgomez@mail.com")

##Mostrar el tipo de dato que es un objeto
int = 10
print(type(int))