import os
from Pelicula import Pelicula
class List_Peliculas:
    pelis = []

    @classmethod
    def agregar_pelicula(cls,nom):
        pelicula = Pelicula()
        pelicula.set_nombre(nom)
        archivo = None
        try:
            archivo = open("Peliculas.txt","a+",encoding="utf8")
            archivo.write(pelicula.get_nombre()+"\n")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        else:
            peli = Pelicula()
            peli.set_nombre(nom)
            List_Peliculas.pelis.append(peli)
            print("Se agrego correctamente...")
            archivo.close()

    @classmethod
    def leer_peliculas(cls):
        ruta = "Peliculas.txt"
        archivo = None
        lineas = []
        try:
            if  os.path.exists(ruta):
                archivo = open(ruta,"r",encoding="utf8")
                lineas = archivo.readlines()
            else:
                archivo = open(ruta,"x")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        else:
            if len(lineas) > 0:
                for x in lineas:
                    peli = Pelicula()
                    peli.set_nombre(x)
                    List_Peliculas.pelis.append(peli)
                    archivo.close()

    @classmethod
    def eliminar_catalogo(cls):
        try:
            os.remove("Peliculas.txt")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
        else:
            List_Peliculas.pelis.clear()
            print("Se elimino exitosamente el catalogo...")

    def __str__(self):
        campo =""
        for x in List_Peliculas.pelis:
            campo += x.__str__() + "\n"

        return f"{campo}"