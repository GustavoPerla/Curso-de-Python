#importante antes de esto ver si estan instaladas las librerias en Python

import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "31928264As",
    database = "personas_db"
)

cursor = personas.cursor()

sentencia = ("DELETE FROM personas where id=%s") #Si no se ponen campos actualiza todos

valores = (1,)#Tiene que ser una tupla

cursor.execute(sentencia,valores)

personas.commit()

print("Se a eliminado el registro")

personas.close()