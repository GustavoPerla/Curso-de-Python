
class computadora:
    __contador_computadoras=0

    def __init__(self):
        computadora.__contador_computadoras+=1
        self.__id_computadoras = computadora.__contador_computadoras

    def set_nombre(self,nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre
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

    def __str__(self):
        return (f"""Id= {self.__id_computadoras} Nombre: {self.__nombre}
                \tRaton = {self.__raton}
                \tMonitor = {self.__monitor}
                \tTeclado = {self.__teclado}
        """)