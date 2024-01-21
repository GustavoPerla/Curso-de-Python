from DispositivoEntrada import dispositivoEntrada

class teclado(dispositivoEntrada):
    contador_teclado = 0

    def __init__(self, ):
        teclado.contador_teclado += 1
        self.id_teclado += teclado.contador_teclado
        self.disp_entrada = dispositivoEntrada()
        super().
        self.disp_entrada.set_marca(input("Ingrese la marca del teclado: "))
        self.disp_entrada.set_tipoEntrada(input("Ingrese el tipo de enrada del teclado: "))


    def __str__(self):
        pass