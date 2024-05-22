from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories import status_animal_repositories as crud
from ..schemas import status_animal_schema as schemas
from ..database.database import get_db

router = APIRouter()

@router.post("/status_animal/", response_model=schemas.StatusAnimalCreate)
def create_status_animal(status_animal: schemas.StatusAnimalCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_status_animal(db=db, status_animal=status_animal)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status_animal/{id}", response_model=schemas.StatusAnimalBase)
def read_status_animal(id_status_animal: str, db: Session = Depends(get_db)):
    db_status_animal = crud.get_status_animal(db, id_status_animal=id_status_animal)
    if db_status_animal is None:
        raise HTTPException(status_code=404, detail="status_animal not found")
    return db_status_animal

@router.get("/status_animal/", response_model=List[schemas.StatusAnimal])
def read_status_animal(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    status_animal = crud.get_status_animal(db, skip=skip, limit=limit)
    return status_animal

@router.put("/status_animal/{id}", response_model=schemas.StatusAnimal)
def update_status_animal(id: int, status_animal: schemas.StatusAnimalCreate, db: Session = Depends(get_db)):
    return crud.update_status_animal(db=db, id=id, status_animal=status_animal)

@router.delete("/status_animal/{id}", response_model=schemas.StatusAnimal)
def delete_status_animal(id: int, db: Session = Depends(get_db)):
    return crud.delete_status_animal(db=db, id=id)
