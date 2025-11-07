from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FichaClinica(Base):
    __tablename__ = 'ficha_clinica'
    id = Column(Integer, primary_key=True)
    id_paciente = Column(Integer, nullable=False)
    historial_clinico = Column(String(250), nullable=False)
    