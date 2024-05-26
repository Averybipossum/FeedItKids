from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repositories import animal_repositories as crud
from src.schemas import animal_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/animal/")
async def create_animal(animal: schemas.AnimalBase, db: Session = Depends(get_db)):
    try:
        return crud.create_animal(db=db, animal=animal)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/animal/{id_animal}", response_model=schemas.AnimalBase)
def read_animal(id_animal: int, db: Session = Depends(get_db)):
    db_animal = crud.get_animal(db, animal_id = id_animal)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="animal not found")
    return db_animal

@router.put("/animal/{id_animal}", response_model=schemas.AnimalBase)
async def update_animal(id_animal: int, animal: schemas.AnimalBase, db: Session = Depends(get_db)):
    return crud.update_animal(db=db, id_animal=id_animal, animal=animal)

@router.delete("/animal/{id_animal}", response_model=schemas.AnimalBase)
async def delete_animal(id_animal: int, db: Session = Depends(get_db)):
    return crud.delete_animal(db=db, id_animal=id_animal)
