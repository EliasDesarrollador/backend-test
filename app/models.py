
# Importamos  las herramientas necesarias de SQLAlchemy
from sqlalchemy import Column, Integer ,String, ForeighKey
from sqlalchemy.orm import relarionship
from app.database import Base

#Modelo  para la tabla de usuarios 
class User(Base):
    __tablename__ = "users" # Nombre de  la tabla en la base

    # Columnas de la tabla  
    id = Column(Integer, primary_key=True, index=True) # ID autoincremental 
    titulo = Column(String, nullable=False) # Titulo de la tarea
    descripcion = Column(String ) #Descripcion
    estado = Column(String, default ="pendiente") # Estado por  defecto
    id_usuario = Column(Integer, ForeignKey("users.id")) # Clave foranea(usuario dueno) 

    #Relacion inversa con usuarios 
    usuario = relarionship("User", back_populates="tareas")
    