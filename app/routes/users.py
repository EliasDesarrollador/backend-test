
from Fastapi import APIRouter , Depends, HTTPException
from sqlalchemy.orm import Session 


#Importamos los esquemas (validacion)
from app.schemas import UserCreate , User
#Importamos  los modelos  de BD 
from app.models import User as UserModel
#Dependencias DB 
from app.database import get_db


#Creamos el router  especifico  para  usuarios
router = APIRouter(
    prefix="/users",      #Todas las rutas tendran /users al inicio 
    tags=["Usuarios"]    # para documentacion de  Swagger
)


