from modelos.direccion import Direccion

class Paciente(Direccion):
    def __init__(self,id,nombre,edad,id_direccion,rut):
        super().__init__(id_direccion)
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
