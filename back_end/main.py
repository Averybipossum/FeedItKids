from fastapi import FastAPI
from back_end.src.db_setup import engine

from src.models.Alimento_model import Alimentos, Status
from src.models.Animal_model import Animal, ConsumoAnimal, StatusAnimal
from back_end.src.models.Usuario_model import Usuario
from back_end.src.models.Objetivo_model import Objetivos, ObjetivoCompleto

app = FastAPI()

# Define database initialization and table creation as a separate function
def initialize_database():
    # Create all tables if they do not exist
    Alimentos.Base.metadata.create_all(bind=engine)
    Status.Base.metadata.create_all(bind=engine)
    Animal.Base.metadata.create_all(bind=engine)
    ConsumoAnimal.Base.metadata.create_all(bind=engine)
    StatusAnimal.Base.metadata.create_all(bind=engine)
    Usuario.Base.metadata.create_all(bind=engine)
    Objetivos.Base.metadata.create_all(bind=engine)
    ObjetivoCompleto.Base.metadata.create_all(bind=engine)

# Call the database initialization function before starting the FastAPI application
initialize_database()

@app.get("/")
async def root():
    return {"message": "teste"}