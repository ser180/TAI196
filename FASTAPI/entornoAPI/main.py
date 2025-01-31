from fastapi import FastAPI
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

@app.get('/promedio', tags=['Promedio'])
def promedio():
    return 20.1

#endPoint Parametro obligatorio
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultaUsuario(id:int):
    #Conectarse a la BD
    #Hacer consulta y retornar resultset
    return{"Se encontro el usuario": id}

#endPoint Parametro opcional
@app.get('/usuario/', tags=['Parametro opcional'])
def consultaUsuario2(id: Optional[int]= None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Mensaje":"Usuario encontrado", "Usuario": usuario}
        return{"Mensaje":f"No se encontro el id: {id}"}
    else:
        return{"Mensaje":"No se proporciono un Id"}

#--------------------------------------------------------------------------------------

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}