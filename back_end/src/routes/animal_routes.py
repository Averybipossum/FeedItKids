from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repositories import animal_repositories as crud
from src.schemas import animal_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/animal/", response_model=schemas.AnimalResponse)
async def create_animal(animal: schemas.AnimalBase, db: Session = Depends(get_db)):
    try:
        created_animal = crud.create_animal(db=db, animal=animal)
        return schemas.AnimalResponse(id_animal=created_animal.id_animal)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/animal/{id_animal}", response_model=schemas.AnimalResponse)
def read_animal(id_animal: int, db: Session = Depends(get_db)):
    db_animal = crud.get_animal(db, animal_id = id_animal)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="animal not found")
    return db_animal

@router.put("/animal/{id_animal}", response_model=schemas.AnimalResponse)
async def update_animal(id_animal: int, animal_update: schemas.AnimalUpdate, db: Session = Depends(get_db)):
    db_animal = crud.update_animal(db=db, animal_id=id_animal, animal_update=animal_update)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return db_animal

@router.delete("/animal/{id_animal}", response_model=schemas.AnimalResponse)
async def delete_animal(id_animal: int, db: Session = Depends(get_db)):
    db_animal = crud.get_animal(db, id_animal)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    # Delete the animal
    deleted_animal = crud.delete_animal(db=db, animal_id=id_animal, animal_delete=schemas.AnimalUpdate(id_animal=id_animal))
    if deleted_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    return db_animal