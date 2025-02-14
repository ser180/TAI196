from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title='Mi primer API 196',
    description = 'Sergio Ramón Olmedo Soto',
    version = '1.0.1'
)

usuarios=[
    {"id":1,"nombre":"Sergio","edad":20},
    {"id":2,"nombre":"Ayrton","edad":21},
    {"id":3,"nombre":"Carlos","edad":20},
    {"id":4,"nombre":"Noel","edad":23},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FastAPI':'Sergio Ramón'}

#endpoint Consultar todos
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {"Usuarios Registrados ": usuarios}

#endpoint Para Agregar usuarios
@app.post('/usuario/',tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: dict ):
    for usr in usuarios: #verificar la lista por medio de una validación
        if usr["id"] == usuarionuevo.get("id"): #Si se repite el id manda un error por medio del raise
            raise HTTPException(status_code=400, detail="El id ya esta registrado") 
    usuarios.append(usuarionuevo) #Agrega un usuario nuevo a la lista por medio del append
    return usuarionuevo #Devuelve como respuesta positiva el usuario guardado

#endpoint PUT
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def ActualizarUsuario(id: int, usuario_actualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuario_actualizado)
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