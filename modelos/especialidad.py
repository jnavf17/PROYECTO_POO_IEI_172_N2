from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Especialidad(Base):
    __tablename__ = 'especialidad'
    id = Column(Integer, primary_key=True)
    especialidad = Column(String(250), nullable=False)
    despripcion = Column(String(250), nullable=False)
    