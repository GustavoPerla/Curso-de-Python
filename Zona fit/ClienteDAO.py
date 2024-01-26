from Cliente import Cliente
from Conexion import Conexion
from Funciones import *


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM personas"
    INSERTAR = "INSERT INTO personas(nombre, apellido, membresia) VALUES(%s,%s,%s)"
    ACTUALIZAR = "UPDATE personas SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM personas WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            regis = cursor.fetchall()

            #Mapeo de la clase_tabla clientes
            clientes = []
            for x in regis:
                cliente = Cliente()

                cliente.set_nombre(x[1])
                cliente.set_apellido(x[2])
                cliente.set_id(x[0])
                cliente.set_membresia(x[3])
                clientes.append(cliente)

            return clientes
        except Exception as e:
            print(f"Ocurrio un error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cliente = ingresar_cliente()

            cursor.execute(cls.INSERTAR, cliente)
            cursor.fetchall()
            conexion.commit()
            return cursor.rowcount ### Cuenta la cantidad de insert que se hacen
        except Exception as e:
            print(f"Ocurrio un error al insertar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cliente = actualizar_cliente()
            cursor.execute(cls.ACTUALIZAR, cliente)
            cursor.fetchall()
            conexion.commit()
            return cursor.rowcount  ### Cuenta la cantidad de insert que se hacen
        except Exception as e:
            print(f"Ocurrio un error al actualizar clientes: {e}")

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cliente = (eliminar_cliente(),)
            cursor.execute(cls.ELIMINAR, cliente)
            cursor.fetchall()
            conexion.commit()
            return cursor.rowcount  ### Cuenta la cantidad de insert que se hacen
        except Exception as e:
            print(f"Ocurrio un error al actualizar clientes: {e}")

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)