## Argumentos variables

#*args -> es una tupla

#**kwargs -> es un diccionario(map)
def super_heroe(nombre,*args):
    print(f"El superheroe es: {nombre} y sus poderes son: {args}") ## *args es para una cantidad indefinida de argumentos
## es opcional enviar argumentos variables
#Llamamos a la funcion

super_heroe("Spederman","Instinto aracnido","Telaraña")
super_heroe("Ironman","Armadura","Playboy","Millonario")