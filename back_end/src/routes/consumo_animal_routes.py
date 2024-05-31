from typing import List
from fastapi import APIRouter, Depends, HTTPException
from psycopg2 import IntegrityError, OperationalError
from sqlalchemy.orm import Session
from src.models import Animal_model as models

from src.repositories import consumo_animal_repositories as crud
from src.schemas import consumo_animal_schema as schemas
from src.database.database import get_db

router = APIRouter()

@router.post("/consumo", response_model=schemas.ConsumoAnimal)
def create_consumo(consumo: schemas.ConsumoAnimalBase, db: Session = Depends(get_db)):
    try:
        return crud.create_consumo(db=db, consumo_animal=consumo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/consumo/{id_consumo}", response_model=schemas.ConsumoAnimalBase)
def read_consumo(id_consumo: int, db: Session = Depends(get_db)):
    db_consumo = crud.get_consumo(db, id_consumo=id_consumo)
    if db_consumo is None:
        raise HTTPException(status_code=404, detail="consumo not found")
    return db_consumo

@router.get("/consumo", response_model=List[schemas.ConsumoAnimal])
def read_consumo(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    consumo = crud.get_consumos(db, skip=skip, limit=limit)
    return consumo

# @router.put("/consumo/{id_consumo}", response_model=schemas.ConsumoAnimal)
# def update_consumo(id_consumo: int, consumo: schemas.ConsumoAnimalBase, db: Session = Depends(get_db)):
#     return crud.update_consumo(db=db, id_consumo=id_consumo, consumo=consumo)

@router.delete("/consumo/{id_consumo}", response_model=schemas.ConsumoAnimal)
def delete_consumo(id_consumo: int, db: Session = Depends(get_db)):
    return crud.delete_consumo_animal(db=db, id_consumo=id_consumo)


# @router.post("/consumo/{id_alimento}", response_model=schemas.ConsumoRequest)
# def create_consumo_by_alimento(consumo: schemas.ConsumoAnimalBase, db: Session = Depends(get_db)):
#     try:
#         db_alimento = def get_status_by_grupo_alimento(db:Session, grupo_alimento: str):
#             return db.query(models.StatusAlimento).filter_by(grupo_alimento = grupo_alimento)
#         return crud.create_consumo_by_id_status(db=db, consumo_animal=consumo, id_status=)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))