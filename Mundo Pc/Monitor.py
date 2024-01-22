
class monitor():
    contador_monitor = 0

    def __init__(self):
        monitor.contador_monitor+=1
        self.__id_monitor = monitor.contador_monitor

    def __str__(self):
      return (f"Id: {self.__id_monitor}, "
              f"Marca: {self.__marca}, "
              f"Tamaño: {self.__tamanio}\"")

    def set_marca(self,marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_tam(self,tam):
        self.__tamanio=tam

    def get_tam(self):
        return self.__tamanio