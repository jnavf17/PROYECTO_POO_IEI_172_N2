from iu.menus import menu_principal, menu_trabajos,menu_configuracion,sub_menu_comunas
from datos.guardar_datos import guardar_comuna
from negocio import obtener_listado_comunas,crear_comuna,modificar_comuna
from auxiliares import nombre_aplicacion, numero_version

# Definición de constantes literales para menú
seleccionar_opcion = 'Seleccione su opción [0-4]: '
opcion_incorrecta = 'Opción Incorrecta, ingrese nuevamente...'
volver_menu_principal = 'Volviendo al menú principal...'

print(f'{nombre_aplicacion} {numero_version}')
while True:
    print()
    menu_principal()
    opcion = input('Seleccione su opción [0-5]: ')
    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        while True:
            menu_trabajos()
            opcion_configuracion = input('Seleccione su opción [0-5]: ')
            if opcion_configuracion == '1':
                pass
            elif opcion_configuracion == '2':
                pass
            elif opcion_configuracion == '3':
                pass
            elif opcion_configuracion == '4':
                pass
            elif opcion_configuracion == '0':
                print('Volviendo al menú principal...')
                break
            else:
                print(opcion_incorrecta)
    elif opcion == '5':
        while True:
            menu_configuracion()
            opcion_configuracion = input(seleccionar_opcion)
            if opcion_configuracion == '1':
                while True:
                    sub_menu_comunas()
                    opcion_comuna = input(seleccionar_opcion)
                    if opcion_comuna == '1':
                        obtener_listado_comunas()
                    elif opcion_comuna == '2':
                        crear_comuna()
                    elif opcion_comuna == '3':
                        modificar_comuna()
                    elif opcion_comuna == '4':
                        pass
                    elif opcion_comuna == '0':
                        print('Volviendo al menú configuración...')
                        break
                    else:
                        print(opcion_incorrecta)
            elif opcion_configuracion == '0':
                print(volver_menu_principal)
                break
            else:
                print(opcion_incorrecta)
    elif opcion == '0':
        print('Saliendo...')
        break
    else:
        print(opcion_incorrecta)
        
# from modelos.comuna import Comuna
# from datos.obtener_datos import obtener_lista_objetos
# from negocio.negocio_comuna import obtener_comuna_nombre

# from prettytable import PrettyTable


# def trabajo_comunas():
#     tabla_comunas = PrettyTable()
#     tabla_comunas.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
#     comuna = Comuna
#     listado_comunas = obtener_lista_objetos(comuna)
#     if listado_comunas:
#         for comuna in listado_comunas:
#             tabla_comunas.add_row(
#                 [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
#             # print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')
#         print(tabla_comunas)


# def buscar_comuna():
#     tabla = PrettyTable()
#     tabla.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
#     nombre_comuna = input('Ingrese nombre de comuna a buscar: ')
#     if nombre_comuna != '':
#         comuna = obtener_comuna_nombre(nombre_comuna)
#         if comuna is not None:
#             tabla.add_row(
#                 [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
#             print(tabla)


# # trabajo_comunas()
# # buscar_comuna()
