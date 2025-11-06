# from modelos.direccion import Direccion

# class Paciente(Direccion):
#     def __init__(self,id,nombre,edad,id_direccion,rut):
#         super().__init__(id_direccion)
#         self.id = id
#         self.nombre = nombre
#         self.edad = edad
#         self.rut = rut

from sqlalchemy import Column, Integer,String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'Paciente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=True)
    edad = Column(Integer, nullable=True)
    id_direccion = Column(Integer, nullable=True)
    rut = Column(String(10), nullable=True)