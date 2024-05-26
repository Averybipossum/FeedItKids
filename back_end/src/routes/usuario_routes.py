from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import usuario_schema as schemas
from src.repositories import usuario_repositories as repository
from typing import Annotated, List
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from sqlalchemy.orm import Session
from src.database.database import get_db

router = APIRouter()


db_dependency = Annotated[Session, Depends(get_db)]

# Rotas da API
@router.post("/", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def create_user(usuario: schemas.UsuarioBase, db: db_dependency):
    return repository.create_usuario(db, usuario)

@router.get("/{id_usuario}", response_model=schemas.UsuarioResponse)
async def read_user(id_usuario: int, db: db_dependency):
    db_usuario = repository.get_usuario(db, id_usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_usuario

@router.delete("/{id_usuario}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id_usuario: int, db: db_dependency):
    repository.delete_usuario(db, id_usuario)
    return None

