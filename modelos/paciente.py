from sqlalchemy import Column, Integer,String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Paciente(Base):
    __tablename__ = 'Paciente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=True)
    edad = Column(Integer, nullable=True)
    id_direccion = Column(Integer, nullable=True)
    rut = Column(String(10), nullable=True)