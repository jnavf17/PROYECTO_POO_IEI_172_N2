from datos.conexion import Session
from sqlalchemy import func
from modelos.comuna import Comuna
from modelos.marca import Marca
from modelos.modelo import Modelo

sesion = Session()


def guardar_comuna():
    nombre = input('Ingrese nombre comuna: ')
    codigo = input('Ingrese código de comuna: ')
    nueva_comuna = Comuna(
        nombre_comuna=nombre.title(),
        codigo_comuna=codigo)
    sesion.add(nueva_comuna)
    try:
        sesion.commit()
        print(
            f"La comuna '{nueva_comuna.nombre_marca}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la comuna: {e}")
    finally:
        sesion.close()