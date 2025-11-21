
from fastapi import APIRouter , Depends, HTTPException
from sqlalchemy.orm  import Session 

from app.schemas import TaskCreate, Task 
from app.models import Task as TaskModel, User  as UserModel 
from app.database import get_db


#Router para  tareas 
router = APIRouter(
    prefix="/tasks",    # Todas las rutas empiezan con /tasks 
    tags=["Tareas"]
)



#   -----------------------------------------------------------
#                        CREAR UNA TAREA 
# ------------------------------------------------------------
