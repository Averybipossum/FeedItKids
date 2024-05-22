from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..repositories import objetivos_repositories as crud
from ..schemas import objetivos_schema as schemas
from ..database.database import get_db

router = APIRouter()

@router.post("/objetivos/", response_model=schemas.Objetivos)
def create_objetivos(objetivo: schemas.ObjetivosCreate, db: Session = Depends(get_db)):
    return crud.create_objetivos(db=db, objetivo=objetivo)

@router.get("/objetivos/{id_objetivo}", response_model=schemas.Objetivos)
def read_objetivo(id_objetivo: int, db: Session = Depends(get_db)):
    db_objetivo = crud.get_objetivo(db, id_objetivo=id_objetivo)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo not found")
    return db_objetivo

@router.get("/objetivos/", response_model=List[schemas.Objetivos])
def read_objetivos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    objetivos = crud.get_objetivos(db, skip=skip, limit=limit)
    return objetivos

@router.put("/objetivos/{id_objetivo}", response_model=schemas.Objetivos)
def update_objetivo(id_objetivo: int, objetivo: schemas.ObjetivosUpdate, db: Session = Depends(get_db)):
    return crud.update_objetivo(db=db, id_objetivo=id_objetivo, objetivo=objetivo)

@router.delete("/objetivos/{id_objetivo}", response_model=schemas.Objetivos)
def delete_objetivo(id_objetivo: int, db: Session = Depends(get_db)):
    return crud.delete_objetivo(db=db, id_objetivo=id_objetivo)
