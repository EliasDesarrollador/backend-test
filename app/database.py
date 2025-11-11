# Importamos  modulos de SQLALchemy para crear la conexion y mannejar sesiones 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL  de la base de datos . En este caso usamos archivo SQLite (archivo local)
SQALCHEMY_DATABASE_URL ="sqlite:///./test.db"

# Creamos e motor  de conexion (engine)
#  "connect_args" solo  se usa  con SQLite para permitir  acceso desde distintos  hilos
engine = create_engine(
    SQALCHEMY_DATABASE_URL, connect_args=("check_same_thread": False)
)