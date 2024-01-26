class Cliente:

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_id(self,id):
        self.id=id

    def get_id(self):
        return self.id

    def set_apellido(self,apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_membresia(self, mem):
        self.membresia = mem

    def get_membresia(self):
        return self.membresia

    def __str__(self):
        return f"Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresia: {self.membresia}"