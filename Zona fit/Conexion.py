from mysql.connector import pooling
from mysql.connector import Error

##Un pool de conexiones se ultiliza para poder tener mas de una conexion en simultaneo en la BD

class Conexion:
    DATABASE = "zona_fit_db" ## En mayuscula se considera en python que no se debe cambiar el valor de la variable
    USERNAME = "root"
    PASSWORD = "31928264As"
    DB_PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host =  cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error en la conexion a la BD: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()