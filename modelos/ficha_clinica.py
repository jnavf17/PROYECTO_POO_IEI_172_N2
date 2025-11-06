# from modelos.paciente import Paciente

# class FichaClinica(Paciente):
#     def __init__(self,id,id_paciente,historial_medico):
#         super().__init__(id_paciente)
#         self.id = id
#         self.historial_medico = historial_medico

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Marca(Base):
    __tablename__ = 'ficha_clinica'
    id = Column(Integer, primary_key=True)
    id_paciente = Column(Integer, nullable=False)
    historial_clinico = Column(String(250), nullable=False)
    