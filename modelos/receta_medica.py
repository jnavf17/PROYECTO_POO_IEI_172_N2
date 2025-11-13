from sqlalchemy import Column, Integer,String, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RecetaMedica(Base):
    __tablename__ = 'Recetamedica'
    id = Column(Integer, primary_key=True)
    detalle = Column(String(250), nullable=True)
    fecha = Column(Date(), server_default=func.now())
    id_paciente = Column(Integer, nullable=True)
    id_doctor = Column(Integer, nullable=True)
    