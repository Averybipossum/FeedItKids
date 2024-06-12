from typing import Dict
from psycopg2 import DataError, IntegrityError
from sqlalchemy.orm import Session
from src.models import Animal_model as models
from src.schemas import animal_schema as schemas

# CRUD BANCO DE DADOS 


def get_animal(db: Session, animal_id: int):
    return db.query(models.Animal).filter(models.Animal.id_animal == animal_id).first()


def get_animals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Animal).offset(skip).limit(limit).all()

def create_animal(db: Session, animal: schemas.AnimalBase):
    try:
        db_animal = models.Animal()
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)
        return db_animal
    except (IntegrityError, DataError) as e:
        raise Exception(f"Error creating animal: {str(e)}")


def update_animal(db: Session, animal_id: int, animal_update: schemas.AnimalUpdate):
    db_animal = db.query(models.Animal).filter(models.Animal.id_animal == animal_id).first()
    if not db_animal:
        return None
    for field, value in animal_update.dict(exclude_unset=True).items():
        setattr(db_animal, field, value)
    db.commit()
    db.refresh(db_animal)
    return db_animal




def delete_animal(db: Session, animal_id: int, animal_delete: schemas.AnimalBase):
    db_animal = db.query(models.Animal).filter(models.Animal.id_animal == animal_id).first()
    if not db_animal:
        return None
    db.delete(db_animal)
    db.commit()
    return db_animal
