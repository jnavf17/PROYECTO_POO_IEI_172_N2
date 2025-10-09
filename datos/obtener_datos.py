from datos.conexion import Session
from modelos.comuna import comuna
from sqlalchemy import func

sesion = Session()

listado_test = sesion.query(comuna).all()