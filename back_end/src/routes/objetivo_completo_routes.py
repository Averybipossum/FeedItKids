from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.repositories import objetivo_completo_repositories as crud
from src.schemas import objetivo_completo_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/objetivoCompleto/", response_model=schemas.ObjetivoCompleto)
def create_objetivoCompleto(objetivo: schemas.ObjetivoCompletoBase, db: Session = Depends(get_db)):
    return crud.create_objetivo_completo(db=db, objetivo = objetivo)

@router.get("/objetivoCompleto/{id_objetivo}", response_model=schemas.ObjetivoCompleto)
def read_objetivoCompleto(id_objetivo: int, db: Session = Depends(get_db)):
    db_objtivos = crud.get_objetivo_completo(db, id_objetivo = id_objetivo)
    if db_objtivos is None:
        raise HTTPException(status_code=404, detail="Objetivo not found")
    return db_objtivos

@router.get("/objetivoCompleto/", response_model=List[schemas.ObjetivoCompleto])
def read_objetivosCompleto(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    objetivos = crud.get_objetivos_completo(db, skip=skip, limit=limit)
    return objetivos

@router.put("/objetivoCompleto/{id_objetivo}",response_model=schemas.ObjetivoCompleto)
def update_objetivo(id_objetivo: int, objetivo: schemas.ObjetivoCompletoUpdate, db: Session = Depends(get_db)):
    return crud.update_objetivo_completo(db=db, id_objetivo = id_objetivo, objetivo = objetivo)

@router.delete("/objetivoCompleto/{id_objetivo}", response_model=schemas.ObjetivoCompletoUpdate)
def delete_objetivo(id_objetivo: int, db: Session = Depends(get_db)):
    return crud.delete_objetivo_completo(db=db, id_objetivo=id_objetivo)
