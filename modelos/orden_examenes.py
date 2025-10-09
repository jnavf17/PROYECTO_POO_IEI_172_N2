from modelos.paciente import Paciente
from modelos.doctor import Doctor
from modelos.cita_medica import Cita_medica

class RecetaMedica(Paciente,Doctor,Cita_medica):
    def __init__(self,id,fecha,id_paciente,id_doctor,id_cita_medica):
        super().__init__(id_paciente)
        super().__init__(id_doctor)
        super().__init__(id_cita_medica)
        self.id = id
        self.fecha = fecha