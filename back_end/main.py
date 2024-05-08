from fastapi import FastAPI

from back_end.src.database.db_setup import engine
from .src.database.models import User_model, Animal_model, Alimento_model

User_model.Base.metadata.create_all(bind = engine)
Animal_model.Base.metadata.create_all(bind = engine)
Alimento_model.Base.metadata.create_all(bind = engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "teste"}