from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repositories import status_repositories as crud
from src.schemas import status_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/status/", response_model=schemas.StatusCreate)
def create_usuario(status: schemas.StatusCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_status(db=db, status=status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status/{id_status}", response_model=schemas.StatusBase)
def read_status(id_status: int, db: Session = Depends(get_db)):
    db_status = crud.get_status(db, id_status=id_status)
    if db_status is None:
        raise HTTPException(status_code=404, detail="status not found")
    return db_status

@router.get("/status/", response_model=List[schemas.Status])
def read_status(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    status = crud.get_status(db, skip=skip, limit=limit)
    return status

@router.put("/status/{id_status}", response_model=schemas.StatusCreate)
def update_status(id_status: int, status: schemas.StatusCreate, db: Session = Depends(get_db)):
    return crud.update_status(db=db, id_status=id_status, status=status)

@router.delete("/status/{id_status}", response_model=schemas.Status)
def delete_status(id_status: int, db: Session = Depends(get_db)):
    return crud.delete_status(db=db, id_status=id_status)
