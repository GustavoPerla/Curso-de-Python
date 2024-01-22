class Snack:
    cont_snacks = 0

    def __init__(self):
        Snack.cont_snacks += 1
        self.id_snacks = Snack.cont_snacks

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_precio(self,precio):
        self.__precio=precio

    def get_precio(self):
        return self.__precio

    def get_id(self):
        return self.id_snacks

    def __str__(self):
        return (f"Snack: {self.id_snacks}\t"
                f"Nombre: {self.__nombre}\t"
                f"Precio: {self.__precio}")