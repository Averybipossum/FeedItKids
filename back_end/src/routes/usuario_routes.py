from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories import usuario_repositories as crud
from ..schemas import usuario_schema as schemas
from ..database.database import get_db

router = APIRouter()

@router.post("/usuarios/", response_model=schemas.UsuarioCreate)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db=db, usuario=usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/usuarios/{id_usuario}", response_model=schemas.UsuarioBase)
def read_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, id_usuario=id_usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@router.get("/usuarios/", response_model=List[schemas.UsuarioBase])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.put("/usuarios/{id_usuario}", response_model=schemas.UsuarioUpdate)
def update_usuario(id_usuario: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    return crud.update_usuario(db=db, id_usuario=id_usuario, usuario=usuario)

@router.delete("/usuarios/{id_usuario}", response_model=schemas.UsuarioBase)
def delete_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return crud.delete_usuario(db=db, id_usuario=id_usuario)
