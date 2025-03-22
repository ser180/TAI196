from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
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

usuarios=[
    {"id":1,"nombre":"Sergio","edad":20, "correo":"sergio@example.com"},
    {"id":2,"nombre":"Ayrton","edad":21, "correo":"ayrton@example.com"},
    {"id":3,"nombre":"Carlos","edad":20, "correo":"carlos@example.com"},
    {"id":4,"nombre":"Noel","edad":23, "correo":"noel@example.com"},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FastAPI':'Sergio Ramón'}

#endpoint para generar Token usando TokenGen
@app.post('/auth',tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'sergio@example.com' and autorizado.passw == '123456789':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso":"Usuario no Autorizado"}


#endpoint Consultar todos (GET)
@app.get('/usuarios', dependencies=[Depends(BearerJWT())] ,response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endpoint Para Agregar usuarios (POST)
@app.post('/usuarioX/', response_model= modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario ):
    db = Session()
    try:
        #Insert
        db.add(User(**usuarionuevo.model_dump()))
        db.commit
        return JSONResponse(status_code=201, content={"Mensaje":"Usuario Guardado","Usuario":usuarionuevo.model_dump()})
# Mensaje de error si algo sale mal
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje":"Usuario No Guardado","Excepcion":str(e)})
#Cierra la base de datos
    finally:
        db.close()


#endpoint PUT
@app.put('/usuario/{id}',  response_model= modelUsuario, tags=['Operaciones CRUD'])
def ActualizarUsuario(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

    
#endpoint DELETE
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(i) 
            return {"message": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=400, detail="El usuario no existe")

