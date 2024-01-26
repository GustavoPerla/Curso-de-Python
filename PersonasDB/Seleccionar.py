#importante antes de esto ver si estan instaladas las librerias en Python

import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "31928264As",
    database = "personas_db"
)

cursor = personas.cursor() ## se declara este objeto para interactuar con la BD
cursor.execute("SELECT * FROM personas") ## Carga la consulta
resul = cursor.fetchall() ## Ejecuta el comando y devuelve los resultados

for x in resul:
    print(x)

cursor.execute("SELECT nombre, apellido FROM personas") ## Carga la consulta
resul = cursor.fetchall() ## Ejecuta el comando y devuelve los resultados
for x in resul:
    print(x)

personas.close()## Cerrar coneccion