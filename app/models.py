
# Importamos  las herramientas necesarias de SQLAlchemy
from sqlalchemy import Column, Integer ,String, ForeighKey
from sqlalchemy.orm import relarionship
from app.database import Base

#Modelo  para la tabla de usuarios 
class User(Base):
    __tablename__ = "users" # Nombre de  la tabla en la base