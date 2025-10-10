from modelos.doctor import Doctor

class Especialidad(Doctor):
    def __init__(self,id,especialidad,descripcion,id_doctor):
        super().__init__(id_doctor)
        self.id = id
        self.especialidad = especialidad
        self.descripcion = descripcion