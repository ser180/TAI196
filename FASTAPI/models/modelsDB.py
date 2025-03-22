from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__='tb_users'
    # Definir atributos, y agregar parametros especificicos para cada atributo
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    age = Column(Integer)
    email = Column (String)