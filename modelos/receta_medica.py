# from modelos.paciente import Paciente
# from modelos.doctor import Doctor
# from modelos.cita_medica import Cita_medica

# class Recetamedica(Paciente,Doctor,Cita_medica):
#     def __init__(self,id,detalle,fecha,id_paciente,id_doctor,id_cita_medica):
#         super().__init__(id_paciente)
#         super().__init__(id_doctor)
#         super().__init__(id_cita_medica)
#         self.id = id
#         self.detalle = detalle
#         self.fecha = fecha

from sqlalchemy import Column, Integer,String, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'Recetamedica'
    id = Column(Integer, primary_key=True)
    detalle = Column(String(250), nullable=True)
    fecha = Column(Date(timezone=True), server_default=func.now())
    id_paciente = Column(Integer, nullable=True)
    id_doctor = Column(Integer, nullable=True)
    