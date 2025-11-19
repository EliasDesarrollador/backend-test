
#Importamos BaseModel para crear esquemas (validacion 
from pydantic import BaseModel, EmailStr
from typing  import Optional, List 

# ------------SCHEMAS DE TAREAS ---------------

# Esquema base:  define los campos comunes de una tarea 
class TaskBase(BaseModel):
    titulo: str                                                 # Campo obligatorio
    descripcion: Opctional[str] = None  # Campo opcional
    estado: Optional[str] = "pendiente" # Valor por defecto


    # Esquema para crear una nueva tarea  (incluye el ID del usuario )
    class TaksCreate(TaksCreate):
        id_usuario: int
        

        #Esquema para devolver una tarea  al cliente  (incluye el ID )
        class Task(TaskBase):
            id_usuario: int

            class Config: 
                orm_mode = True  # Permite convertir  objetos SQLAlchemy  a JSON 


# ------------SCHEMAS DE USUARIOS ---------------

#Esquema  base : campos comunes del usuario 
class UserBase(BaseModel):
    nombre: str
    email: EmailStr # Validar que el email sea correcto 

#Esquema para  devolver  un usuario con sus tareas 
class User(UserBase):
    contrasena: str

    