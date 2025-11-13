from datos.conexion import sesion
from sqlalchemy import func
from modelos.comuna import Comuna


def crear_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.comit()
        print("El objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la comuna: {e}")
    finally:
        sesion.close()

def modificar_objeto(objeto):
    sesion.merge(objeto)
    try:
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar el objeto: {e}")
    finally:
        sesion.close()

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
            f"La comuna '{nueva_comuna}' se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al guardar la comuna: {e}")
    finally:
        sesion.close()