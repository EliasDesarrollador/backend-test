
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


#   -----------------------------------------------------------
#                         CREAR USUARIO     
# ------------------------------------------------------------

@router .post("/", response_model=User)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):


     # Verifiacmos  si el email ya existe en la db 
     user_exits = db.query(UserModel).filter(UserModel.email == user_data.email).first()
     if user_exits: 
          raise HTTPException(
               status_code =400,
               detail= "El email  ya esta registrado "
          )
     
     # Creamos  un objeto  UserModel 
     new_user = UserModel(
              nombre=user_data.nombre,
              email =user_data.email,
              contrasena= user_data.contrasena      # En prueba guardar si hash 
     )

     # Guardamos en la base de datos  
     db.add(new_user)
     db.commit()
     db.refresh(new_user)  # Actualiza  el objeto  con el ID

     return new_user