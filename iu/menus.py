#Definicion de constantes literales para menú
separador_menu = "================================="
opcion_volver = '[0] Volver'


def menu_principal():
    print()
    print(separador_menu)
    print('Menú Principal')
    print(separador_menu)
    print('[1] .')
    print('[2] .')
    print('[3] .')
    print('[4] .')
    print('[5] .')
    print('[0] Salir')


def menu_trabajos():
    print()
    print(separador_menu)
    print('Menú Trabajos')  
    print(separador_menu)
    print('[1] .')
    print('[2] .')
    print('[3] .')
    print('[4] .')
    print(opcion_volver)

def menu_configuracion():
    print()
    print(separador_menu)
    print('Menú Configuración Aplicación')
    print(separador_menu)
    print('[1] Gestion Comunas.')
    print('[2] Horarios Turnos.')
    print('[3] Gestion Insumos.')
    print('[4] Gestión Personal.')
    print(opcion_volver)

def sub_menu_comunas():
    print()
    print(separador_menu)
    print('Sub-Menú Gestión Comunas')
    print(separador_menu)
    print('[1] Listado Comunas.')
    print('[2] Agregar Comuna.')
    print('[3] Modificar Comuna.')
    print('[4] Eliminar Comuna.')
    print(opcion_volver)