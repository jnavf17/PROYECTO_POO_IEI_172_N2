from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Herramientas necesarias para trabajar con DB
# pip install sqlalchemy
# pip install mysql-connector-python

# Definir cadena de conexion
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port, y database con sus credenciales de DB

cadena_conexion = 'mysql+mysqlconnector://root:@localhost:3306/iei_172_n2'
motordb = create_engine(cadena_conexion)
Session = sessionmaker(bind=motordb)