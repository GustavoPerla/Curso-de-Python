from random import randint

print("*** Sistema de Generador ID Unico ***")
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu Apellido?: ")
nac = input("Cual es tu Año de Nacimiento (YYYY)?: ")

print(f'''Hola {nombre}, habitante de ciudad Gotica!
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {nombre[0:2].upper() + apellido[0:2].upper() + nac[2:len(nac)] + str(randint(0,9999))}
    Felicidades!''')
