#Funciones

def mostrarProd(prod):
    print("Snacks Disponibles:")
    for x in prod:
        print(f"    Id: {x["id"]} -> {x["nombre"]} - Precio: {x["precio"]}")

def mostrarTicket(compra):
    print("*** Ticket de venta ***")
    cont=0.0
    for x in compra:
        print(f"- {x["nombre"]} - ${x["precio"]}")
        cont+=x["precio"]
    print(f"TOTAL -> ${cont}")