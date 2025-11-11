
# Impostamos FastAPI  para crear la aplicacion 
from fastapi import FastAPI
from app.routes import users, tasks  # importamos las rutas de usuarios  y tareas 
from app.database import Base, engine # Importamos la base  y el motor de base de datos 

# Crear las tablas  en la base de datos ( si no extsten)
Base.metadata.create_all(bind-engine)

# Creamos la instancia principal de  FastAPI
app = FastAPI(title = "Backend test API")


# Incluimos las  rutas de usuarios y tareas 
app.include_route(users.router)
app.include_route(tasks.router)

# Ruta principal (inicio)
@app.get("/")
def root():
    return{"message":"API de prueba técnica "} # devuelve un mensaje simple 