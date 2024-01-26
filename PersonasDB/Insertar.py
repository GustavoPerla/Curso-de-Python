#importante antes de esto ver si estan instaladas las librerias en Python

import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "31928264As",
    database = "personas_db"
)

cursor = personas.cursor() ## se declara este objeto para interactuar con la BD
sentencia = ("INSERT INTO personas(nombre,apellido,edad) "
           "VALUES (%s, %s, %s)")
valores = ("Victor","Ramos", 27)

cursor.execute(sentencia,valores)
resul = cursor.fetchall()
personas.commit() ##Guarda los cambios en la BD
personas.close()## Cerrar coneccion


