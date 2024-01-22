from Snack import Snack
from Funciones import *

class Snacks:

    def inventario(nombre, precio):
        inv = Snack()
        inv.set_nombre(nombre)
        inv.set_precio(precio)

        return inv

    __list = [inventario("Papas", 300.0),
              inventario("Refresco",50),
              inventario("Sandwich",120.0)
              ]

    def agregar_snack(self,nombre, precio):
        inven = Snack()

        inven.set_nombre(nombre)
        inven.set_precio(precio)

        Snacks.__list.append(inven)

    def obtener_list(self):
        return Snacks.__list

    def __str__(self):
        campo = ""
        for x in Snacks.__list:
            campo += "\n" + x.__str__()

        return (f"Lista de Snacks: "
                f"\t{campo}")