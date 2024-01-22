from Raton import raton
from Teclado import teclado
from Monitor import monitor
from Computadora import computadora


class orden:
    contador_ordenes = 0

    def __init__(self):
        orden.contador_ordenes+=1
        self.__id_ordenes = orden.contador_ordenes
        self.__listPC = []
    def agregar_computadora(self):
        teclado1 = teclado()
        teclado1.set_marca(input("Ingrese la marca del teclado: "))
        teclado1.set_tipoEntrada(input("Ingrese el tipo de entrada del teclado: "))
        print()
        mouse = raton()
        mouse.set_marca(input("Ingrese la marca del raton: "))
        mouse.set_tipoEntrada(input("Ingrese el tipo de entrada del raton: "))
        print()
        monitor1 = monitor()
        monitor1.set_marca(input("Ingrese la marca del monitor: "))
        monitor1.set_tam(input("Ingrese el tamaño del monitor: "))
        print()
        compu = computadora()
        compu.set_nombre(input("Ingrese el nombre de la computadora: "))
        compu.set_raton(mouse)
        compu.set_monitor(monitor1)
        compu.set_teclado(teclado1)

        self.__listPC.append(compu)

        print("Computadora agregada a la orden..\n")

    def __str__(self):
        compus = ""
        for x in self.__listPC:
            compus+= "\n" + x.__str__()

        return (f"Orden Id: {self.__id_ordenes}  "
                f"Computadora: {compus}")