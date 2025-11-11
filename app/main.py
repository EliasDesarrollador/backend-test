from fastapi import FastAPI
from app.routes import users, tasks
from app.database import Base, engine

# Crear las tablas  en la base de datos 
Base.metadata.create_all(bind-engine)

app = FastAPI(title = "Backend test API")


# Rutas 
app.include_route(users.router)
app.include_route(tasks.router)


@app.get("/")
def root():
    return{"message":"API de prueba técnica "}