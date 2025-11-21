
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
@router.post("/", response_model=Task)
def create_task(task_data: TaskCreate, db : Session = Depends(get_db)):

    #Verficamos  si el usuario dueno  de la tarea existe 
       user = db.query(UserModel).filter(UserModel.id  == task_data.id_usuario).first()

       if not user:
              raise HTTPException(status_code=404, detail = "El usuario no existe , no se puede crear la tarea")
       

       #Creamos la tarea 
       
       new_taks = TaskModel(
              titulo= task_data.titulo, 
              descripcion= task_data.descripcion, 
              estado= task_data.estado,
              id_usuario=task_data.id_usuario
    )
       
       #Guardamos en la BD 
       db.add(new_taks)
       db.commit()
       db.refresh(new_taks)

       return new_taks
