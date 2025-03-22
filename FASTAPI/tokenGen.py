import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='secretkey',algorithm='HS256')
    return token

def validateToken(token:str):
    try:
        data:dict= jwt.decode(token,key='secretkey', algorithms=['HS256'] )
        return data
    #Primera execepcion en caso de que caduque el token
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detalle='El token expiro')
    #Segunda excepcion para token invalido
    except  InvalidTokenError:
        raise HTTPException(status_code=403, detail='Token no autorizado')

