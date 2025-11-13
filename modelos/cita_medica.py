from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Citamedica(Base):
    __tablename__ = 'cita_medica'
    id = Column(Integer, primary_key=True)
    fechayhora = Column(Date(), server_default=func.now())
    motivo = Column(String(255), nullable=False)
    diagnostico = Column(String(255), nullable=False)
    licencia_medica = Column(String(255), nullable=True)
    id_doctor = Column(Integer, nullable=True)
    id_paciente = Column(Integer, nullable=True)

