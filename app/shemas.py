
#Importamos BaseModel para crear esquemas (validacion 
from pydantic import BaseModel, EmailStr
from typing  import Optional, List 

# ------------SCHEMAS DE TAREAS ---------------

# Esquema base:  define los campos comunes de una tarea 
class TaskBase(BaseModel):
    titulo: str                                                 # Campo obligatorio
    descripcion: Opctional[str] = None  # Campo opcional
    estado: Optional[str] = "pendiente" # Valor por defecto
    