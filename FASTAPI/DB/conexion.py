import os 
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Si no 

#Nombre de la BD
dbName = 'usuarios.sqlite'
#Ruta local donde se creara el archivo
base_dir = os.path.dirname(os.path.realpath(__file__)) 
# Nombre y ruta, va a servir para acceder a la BD
dbUrl = f"sqlite:///{os.path.join(base_dir,dbName)}"


#Crea la base de datos en la ruta especifica
engine = create_engine(dbUrl, echo=True)
#Creación de la Session
Session = sessionmaker(bind=engine)
Base = declarative_base()