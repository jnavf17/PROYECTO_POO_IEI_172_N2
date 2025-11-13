from sqlalchemy import Column, Integer, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrdenExamenes(Base):
    __tablename__ = 'Orden_examenes'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date(), server_default=func.now())
    id_doctor = Column(Integer, nullable=True)
    id_paciente = Column(Integer, nullable=True)
    id_cita_medica = Column(Integer, nullable=True)