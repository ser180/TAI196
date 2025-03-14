from pydantic import BaseModel,Field


#Codigo postal, Destino, Peso (gramos)
#class modelEnvios(BaseModel):
  #  codigo_postal:str
   # destino:str
    #peso:int


class modelEnvio(BaseModel):
    codigoPostal:str = Field(..., min_length=5, description='Minimo 5 digitos' )
    destino:str = Field(..., min_length=6, description='Minimo 6 letras' )
    peso:int = Field(..., gt=0, le=500, description='Peso no debe ser menor a 0 gramos y el peso maximo no debe superar los 500 gramos' )