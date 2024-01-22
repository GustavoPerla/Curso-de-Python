from DispositivoEntrada import dispositivoEntrada

class teclado(dispositivoEntrada):
    contador_teclado = 0

    def __init__(self):
        teclado.contador_teclado += 1
        self.__id_teclado = teclado.contador_teclado


    def __str__(self):
        return (f"Id: {self.__id_teclado}, "
                f"Marca: {self.get_marca()}, "
                f"Tipo de entrada: {self.get_tipoEntrada()}")

