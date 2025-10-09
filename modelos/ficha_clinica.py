from modelos.paciente import Paciente

class FichaClinica(Paciente):
    def __init__(self,id,id_paciente,historial_medico):
        super().__init__(id_paciente)
        self.id = id
        self.historial_medico = historial_medico