class Contacto:

    ##constructor
    def __init__(self,nombre, apellido):
        self.__nombre=nombre ##__ esto es un atributo privado y _ es un atributo protected
        self.__apellido = apellido
    def definirAtri(self,celular, email):
        self.__celular = celular
        self.__email = email

    def mostrarAtri(self):
        print(f"""Contacto:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Edad: {self.celular}
        Email: {self.email}
        """)