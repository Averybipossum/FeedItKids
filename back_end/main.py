from fastapi import FastAPI
from src.database.database import engine, Base
from src.models.status_alimento_model import StatusAlimento
from src.models.Animal_model import Animal, ConsumoAnimal, StatusAnimal
from src.models.Usuario_model import Usuario
from src.models.Objetivo_model import Objetivos, ObjetivoCompleto
from src.routes import usuario_routes, objetivos_routes, objetivo_completo_routes,animal_routes,consumo_animal_routes,status_animal_routes,status_routes,auth_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8081/login",
    "http://127.0.0.1:8000/auth/token",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(usuario_routes.router, prefix="/usuarios" ,tags=["usuarios"])
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(objetivos_routes.router, prefix="/objetivos", tags=["objetivos"])
app.include_router(objetivo_completo_routes.router, prefix="/objetivoCompleto", tags=["objetivoCompleto"])
app.include_router(animal_routes.router, prefix="/animal", tags=["animal"])
app.include_router(consumo_animal_routes.router, prefix="/consumo", tags=["consumo"])
app.include_router(status_animal_routes.router, prefix="/status_animal", tags=["status_animal"])
app.include_router(status_routes.router, prefix="/status", tags=["status"])


# Define database initialization and table creation as a separate function
def initialize_database():
    # Create all tables if they do not exist
    Base.metadata.create_all(bind=engine)

# Call the database initialization function before starting the FastAPI application
initialize_database()

@app.get("/")
async def root():
    return {"message": "teste"}
