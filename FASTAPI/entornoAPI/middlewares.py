from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from tokenGen import validateToken

class BearerJWT(HTTPBearer):
    #Uso de asincronia
    async def __call__(self,request:Request):
        #Se coloca el await en donde se espera a que llegue el proceso
        auth=await super().__call__(request)
        #Se gurarda lo que trae la validacion
        data= validateToken(auth.credentials)

        #Realizar validaciones (sintaxis correcta y permisos de acceso)
        if not isinstance(data,dict):
            raise HTTPException(status_code=401, detail='Formato incorrecto en el token')
        if data.get('correo')!= 'sergio@example.com':
            raise HTTPException(status_code=403, detail='Credenciales No Validas')


