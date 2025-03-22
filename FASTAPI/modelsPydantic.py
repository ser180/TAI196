from pydantic import BaseModel, Field, EmailStr

#Modelo para la validacion de datos
class modelUsuario(BaseModel):
    name:str = Field(..., min_length=3 ,max_length=15, description= "Nombre debe contener letras y espacios")
    age:int = Field(..., gt=0, le=130, description="Edad mayor a 0 o menor o igual a 130")
    email:str = Field(..., pattern=r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', example="example@example.com", description="Correo ocupa una estructura como esta example@example.com")

class modelAuth(BaseModel):
    correo:EmailStr
    passw:str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña minimo ocho caracteres")
