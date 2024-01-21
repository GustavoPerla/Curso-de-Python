import Monitor
import Teclado
import Raton

class computadora:
    __contador_computadoras=0

    def __init__(self):
        self.__contador_computadoras+=1
        self.__monitor = Monitor()
        self.__teclado= Teclado()
        self.__raton = Raton()

    def set_monitor(self,monitor):
        self.__monitor=monitor

    def set_raton(self,raton):
        self.__raton= raton

    def set_teclado(self,teclado):
        self.__teclado = teclado

    def get_monitor(self):
        return self.__monitor

    def get_teclado(self):
        return self.__teclado

    def get_raton(self):
        return self.__raton