from sqlalchemy import Column, Integer, DateTime, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Turno(Base):
    __tablename__ = 'Turno'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date(), server_default=func.now())
    hora_inicio = Column(DateTime(timezone=True), server_default=func.now())
    hora_fin = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    id_doctor = Column(Integer, nullable=True)