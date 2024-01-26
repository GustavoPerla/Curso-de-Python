from Cliente import Cliente


def ingresar_cliente():
    cliente = Cliente()
    cliente.set_nombre(input("Ingrese el nombre: "))
    cliente.set_apellido(input("Ingrese el apellido: "))
    cliente.set_membresia(input("Ingrese la membresia: "))

    return cliente.get_nombre(), cliente.get_apellido(), cliente.get_membresia()

def actualizar_cliente():
    cliente = Cliente()
    cliente.set_id(input("Ingrese el id del cliente a actualizar: "))
    cliente.set_nombre(input("Ingrese el nombre: "))
    cliente.set_apellido(input("Ingrese el apellido: "))
    cliente.set_membresia(input("Ingrese la membresia: "))

    return cliente.get_nombre(), cliente.get_apellido(), cliente.get_membresia(), cliente.get_id()

def eliminar_cliente():
    cliente = Cliente()
    cliente.set_id(input("Ingrese el id del cliente a eliminar: "))

    return cliente.get_id()

def menu():
    print("""Menu
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir
    """)