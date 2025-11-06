# from modelos.doctor import Doctor

# class Turno(Doctor):
#     def __init__(self,id,fecha,hora_inicio,hora_fin,id_doctor):
#         super().__init__(id_doctor)
#         self.id = id
#         self.fecha = fecha
#         self.hora_inicio = hora_inicio
#         self.hora_fin = hora_fin

from sqlalchemy import Column, Integer, DateTime, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comuna(Base):
    __tablename__ = 'Turno'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date(timezone=True), server_default=func.now())
    hora_inicio = Column(DateTime(timezone=True), server_default=func.now())
    hora_fin = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    id_doctor = Column(Integer, nullable=True)