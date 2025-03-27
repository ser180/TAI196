from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app= FastAPI(
    title='Mi primer API 196',
    description = 'Sergio Ramón Olmedo Soto',
    version = '1.0.1'
)

#Se encarga de levantar las tablas de la BD
Base.metadata.create_all(bind=engine)


@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FastAPI':'Sergio Ramón'}

#dependencies=[Depends(BearerJWT())]

#endpoint Consultar todos (GET)
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db = Session()
    try:
        #Se guardaran todos los usuarios
        consulta = db.query(User).all()
        return JSONResponse(content = jsonable_encoder(consulta)) 
    
    except Exception as x:
        return JSONResponse(status_code=500, content={"Mensaje":"No fue posible consultar",
                                                      "Excepcion":str(x)}) 
    #Cerrar conexión
    finally:
        db.close()
 

#endpoint Consultar por id (GET)
@app.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarTodos(id:int):
    db = Session()
    try:
        #Busca al usuario donde coincida el id con el que se esta pasando
        consulta = db.query(User).filter(User.id == id).first()
        #Validación que vera si la consulta tiene algo y si no tiene nada no existe le usuario
        if not consulta:
            return JSONResponse(status_code = 404, content = {"Mensaje":"Usuario no encontrado"})
        return JSONResponse(content = jsonable_encoder(consulta)) 
    
    except Exception as x:
        return JSONResponse(status_code=500, content={"Mensaje":"No fue posible consultar",
                                                      "Excepcion":str(x)}) 
    #Cerrar conexión
    finally:
        db.close()



#endpoint Para Agregar usuarios (POST)
@app.post('/usuario/', response_model= modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario ):
    db = Session()
    try:
        #Insert
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"Mensaje":"Usuario Guardado","Usuario":usuarionuevo.model_dump()})
# Mensaje de error si algo sale mal
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje":"Usuario No Guardado","Excepcion":str(e)})
#Cierra la base de datos
    finally:
        db.close()


""" #endpoint PUT
@app.put('/usuario/{id}',  response_model= modelUsuario, tags=['Operaciones CRUD'])
def ActualizarUsuario(id: int, usuario_actualizado: modelUsuario):


    
#endpoint DELETE
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id: int): """



#endpoint para generar Token usando TokenGen
@app.post('/auth',tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'sergio@example.com' and autorizado.passw == '123456789':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso":"Usuario no Autorizado"}
