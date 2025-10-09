from modelos.doctor import Doctor
from modelos.paciente import Paciente

class Citamedica(Doctor,Paciente):
    def __init__(self,id,fechayhora,motivo,diagnostico,licencia_medica,id_doctor,id_paciente):
        super().__init__(id_doctor)
        super().__init__(id_paciente)
        self.id = id
        self.fechayhora = fechayhora
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.licencia_medica = licencia_medica
         

