from DispositivoEntrada import dispositivoEntrada

class raton(dispositivoEntrada):
    contador_ratones = 0

    def __init__(self,marca,tipo):
        raton.contador_ratones += 1
        self.__id_raton = raton.contador_ratones
        super().set_marca(marca)
        super().set_tipoEntrada(tipo)


    def __str__(self):
        return f"Id: {self.__id_raton}, Marca: {self.get_marca()}, Tipo de entrada: {self.get_tipoEntrada()}"
