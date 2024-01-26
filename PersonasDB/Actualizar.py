#importante antes de esto ver si estan instaladas las librerias en Python

import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "31928264As",
    database = "personas_db"
)

cursor = personas.cursor()

sentencia = ("UPDATE personas SET nombre=%s, apellido=%s, edad=%s where id=%s") #Si no se ponen campos actualiza todos

valores = ("Victoria","Flores",45,1)

cursor.execute(sentencia,valores)

personas.commit()

print("se a modificado la informacion")

personas.close()