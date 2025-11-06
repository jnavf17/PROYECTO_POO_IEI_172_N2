# from modelos.doctor import Doctor

# class Especialidad(Doctor):
#     def __init__(self,id,especialidad,descripcion,id_doctor):
#         super().__init__(id_doctor)
#         self.id = id
#         self.especialidad = especialidad
#         self.descripcion = descripcion

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Marca(Base):
    __tablename__ = 'especialidad'
    id = Column(Integer, primary_key=True)
    especialidad = Column(String(250), nullable=False)
    despripcion = Column(String(250), nullable=False)
    