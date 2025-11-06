# from modelos.doctor import Doctor
# from modelos.paciente import Paciente

# class Citamedica(Doctor,Paciente):
#     def __init__(self,id,fechayhora,motivo,diagnostico,licencia_medica,id_doctor,id_paciente):
#         super().__init__(id_doctor)
#         super().__init__(id_paciente)
#         self.id = id
#         self.fechayhora = fechayhora
#         self.motivo = motivo
#         self.diagnostico = diagnostico
#         self.licencia_medica = licencia_medica
         
from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'cita_medica'
    id = Column(Integer, primary_key=True)
    fechayhora = Column(Date(timezone=True), server_default=func.now())
    motivo = Column(String(255), nullable=False)
    diagnostico = Column(String(255), nullable=False)
    licencia_medica = Column(String(255), nullable=True)
    id_doctor = Column(Integer, nullable=True)
    id_paciente = Column(Integer, nullable=True)

