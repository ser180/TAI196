from fastapi import FastAPI, HTTPException
from typing import Optional,List
from models import modelEnvio
from fastapi.responses import JSONResponse

app= FastAPI()

envios=[
    {"codigoPostal":"12345", "destino":"Casa Blanca", "peso":20 }
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Examen Segundo Parcial'}

#Endpoint para eliminar codigo postal
@app.delete('/envio/{codigoPostal}')
def EliminarEnvio(codigoPostal:str):
    for i, env in enumerate(envios):
        if env["codigoPostal"] == codigoPostal:
            envios.pop(i)
            return {"message": "Envio eliminado"}
        raise HTTPException(status_code=400, detial="Envio no encontrado o no existe")

#Endpoint para mostrar todos los envios
@app.get('/envios', response_model= List[modelEnvio])
def ConsultaTodos():
    return envios


@app.post('/envio/',response_model= List[modelEnvio])
def agregarEnvio(envionuevo: modelEnvio):
    for env in envios:
        if env["codigoPostal"]==envionuevo.codigoPostal:
             raise HTTPException(status_code=400, detail="El codigo postal ya esta registrado") 
        envios.append(envionuevo) #Agrega un usuario nuevo a la lista por medio del append
    return envionuevo