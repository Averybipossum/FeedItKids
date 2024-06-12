from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.repositories import status_repositories as crud
from src.schemas import status_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.get("/status/", response_model=List[schemas.StatusResponse])
def get_status_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    statuses = crud.get_status_list(db, skip=skip, limit=limit)
    return statuses

@router.get("/status/{id_status}", response_model=schemas.StatusResponse)
def get_status(id_status: int, db: Session = Depends(get_db)):
    status = crud.get_status(db, id_status)
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@router.post("/status/", response_model=schemas.StatusResponse)
def create_status(status: schemas.StatusBase, db: Session = Depends(get_db)):
    created_status = crud.create_status(db=db, status=status)
    return created_status

@router.put("/status/{id_status}", response_model=schemas.StatusResponse)
def update_status(id_status: int, status_update: schemas.StatusBase, db: Session = Depends(get_db)):
    updated_status = crud.update_status(db=db, id_status=id_status, status_update=status_update)
    if updated_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return updated_status

@router.delete("/status/{id_status}", response_model=schemas.StatusResponse)
def delete_status(id_status: int, db: Session = Depends(get_db)):
    deleted_status = crud.delete_status(db=db, id_status=id_status)
    if deleted_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return deleted_status
