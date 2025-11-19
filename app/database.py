# Importamos  modulos de SQLALchemy para crear la conexion y mannejar sesiones 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL  de la base de datos . En este caso usamos archivo SQLite (archivo local)
SQALCHEMY_DATABASE_URL ="sqlite:///./test.db"

# Creamos e motor  de conexion (engine)
#  "connect_args" solo  se usa  con SQLite para permitir  acceso desde distintos  hilos
engine = create_engine(
<<<<<<< HEAD
    SQALCHEMY_DATABASE_URL, connect_args=("check_same_thread": False)
)

# Creamos una clase para manejar  las sesiones (conexiones) a la base 
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

#Clase base para los modelos (tablas)
Base = declarative_base()

=======
    SQALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Crea una clase para manejar las sesiones (conexiones) a la base 
SessionLocal = sessionmaker(autpcommit= False, autoflush=False, bind=engine)

# Clase base para los modelos  ( tablas)
Base = declarative_base()

#Dependencia que permite obtener las sesion  de base de datos 
#(se usa dentro  de los endpoints)
def get_db():
    db = SessionLocal() # Crea  una sesion nueva
    try:
        yield db  # la devuelve para usarla 
    finally:
        db.close() # Cierra la conexion al terminar 