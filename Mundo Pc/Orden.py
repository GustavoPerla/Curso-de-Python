import Computadora


class orden:
    contador_ordenes = 0

    def __init__(self):
        self.listPC = Computadora()
        self.contador_ordenes+=1

    def agregar_computadora(self):
        pass

    def __str__(self):
        pass