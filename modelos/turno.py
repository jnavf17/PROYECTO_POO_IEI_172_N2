from modelos.doctor import Doctor

class Turno(Doctor):
    def __init__(self,id,fecha,hora_inicio,hora_fin,id_doctor):
        super().__init__(id_doctor)
        self.id = id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        