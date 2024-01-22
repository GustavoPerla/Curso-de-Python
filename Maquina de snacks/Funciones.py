#Funciones
from Snack import Snack
from Snacks import Snacks


def mostrarProd(prod):
    print("Snacks Disponibles:")
    inv = Snacks()
    print(Snacks())

def menu():
    print(f"""Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar producto al inventario
        4. Mostrar inventario
        5. Salir""")
def mostrarTicket(compra):

    mos =""
    print("*** Ticket de venta ***")
    cont=0.0
    for x in compra:
        mos += f"\n- {x.get_nombre()} - ${x.get_precio()}"
        cont += x.get_precio()
    mos += f"\nTOTAL -> ${cont}"

    print(mos)

def Obtener_prod(id):
    s = Snacks()
    list = s.obtener_list()
    for x in list:
        if x.get_id() == id:
            prod = x
            break

    return prod