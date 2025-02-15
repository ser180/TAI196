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

@app.get("/tareas", tags=['Tareas'])
def obtener_tareas():
    return {"Tareas registradas ": Tareas}