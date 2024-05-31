from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repositories import status_animal_repositories as crud
from src.schemas import status_animal_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/status_animal/", response_model=schemas.StatusAnimalBase)
def create_status_animal(status_animal: schemas.StatusAnimalBase, db: Session = Depends(get_db)):
    try:
        return crud.create_status_animal(db=db, status_animal=status_animal)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/status_animal/{id_usuario}", response_model=schemas.StatusAnimal)
def get_status_by_id_animal(id_usuario: int, db: Session = Depends(get_db)):
    db_status_animal = crud.get_status_animal(db, id_usuario=id_usuario)
    if db_status_animal is None:
        raise HTTPException(status_code=404, detail="StatusAnimal not found")
    return db_status_animal

@router.get("/status_animal/", response_model=List[schemas.StatusAnimal])
def read_status_animal(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    status_animal = crud.get_status_animals(db, skip=skip, limit=limit)
    return status_animal


@router.post("/transferir_e_somar_valores/", response_model=schemas.StatusAnimal)
async def transferir_e_somar_valores(grupo_alimento: str, id_usuario: int, db: Session = Depends(get_db)):
    try:
        animal = crud.transferir_e_somar_valores(db=db, grupo_alimento=grupo_alimento, id_usuario=id_usuario)
        return animal
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))