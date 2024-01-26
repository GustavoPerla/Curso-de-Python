from ClienteDAO import ClienteDAO
from Funciones import menu

print("*** Clientes de Zona Fit (GYM) ***")

op = None

while op!=5:
    menu()
    try:
        op = int(input("Escribe tu opcion (1-5):"))

        if 0 < op <6:
            if op == 1:
                clientes = ClienteDAO.seleccionar()
                print("\n*** Listado de clientes: ***")
                for x in clientes:
                    print(x)
            elif op == 2:
                clientesInsertados = ClienteDAO.insertar()
                print(f"Clientes Insertados: {clientesInsertados}")
            elif op == 3:
                clientesActualizados = ClienteDAO.actualizar()
                print(f"Clientes actualizados: {clientesActualizados}")
            elif op == 4:
                print(f"Clientes eliminados: {ClienteDAO.eliminar()}")
            else:
                print("Saliendo de la App...")
        else:
            print("Opcion incorrecta")

    except Exception as e:
        print(f"Ocurrio un error: {e}")