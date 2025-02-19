from fastapi import FastAPI, HTTPException


app= FastAPI(
    title='Practica 04',
    description = 'Sergio Ramón Olmedo Soto',
    version = '1.0.1'
)

Tareas=[
    {"id":1,"titulo":"Estudiar para el examen","descripcion":"estudiar 1 hora", "vencimiento":"14-02-24","estado":"completada"},
    {"id":2,"titulo":"Hacer tarea","descripcion":"Tarea Isay", "vencimiento":"14-03-24","estado":"En espera"}
]

#Obtener tareas
@app.get("/tareas", tags=['Tareas'])
def obtener_tareas():
    return {"Tareas registradas ": Tareas}

#Registrar tareas
@app.post('/tareas/',tags=['Tareas'])
def AgregarTarea(tareasnueva: dict ):
    for usr in Tareas: #verificar la lista por medio de una validación
        if usr["id"] == tareasnueva.get("id"): #Si se repite el id manda un error por medio del raise
            raise HTTPException(status_code=400, detail="El id ya esta registrado") 
    Tareas.append(tareasnueva) #Agrega un usuario nuevo a la lista por medio del append
    return tareasnueva #Devuelve como respuesta positiva el usuario guardado

#Actualizar Tareas
@app.put('/tareas/{id}', tags=['Tareas'])
def ActualizarTarea(id: int, tarea_actualizada: dict):
    for index, usr in enumerate(Tareas):
        if usr["id"] == id:
            Tareas[index].update(tarea_actualizada)
            return Tareas[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")