# class Doctor():
#     def __init__(self,id,especialidad,nombre,licencia):
#         self.id = id
#         self.especialidad = especialidad
#         self.nombre = nombre
#         self.licencia = licencia

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Marca(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    licencia = Column(String(250), nullable=False)
    especialidad = Column(Integer, nullable=False)