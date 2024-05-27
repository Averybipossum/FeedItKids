from sqlalchemy.orm import Session
from src.models import Animal_model as models 
from src.schemas import status_animal_schema as schemas

# CRUD BANCO DE DADOS


def get_status_animal(db: Session, status_animal_id: int):
    return db.query(models.StatusAnimal).filter(models.StatusAnimal.id == status_animal_id).first()


def get_status_animals(db: Session, skip: int = 0, limit: int = 10):

    return db.query(models.StatusAnimal).offset(skip).limit(limit).all()


def create_status_animal(db: Session, status_animal: schemas.StatusAnimalBase):

    db_status_animal = models.StatusAnimal(
        id_animal = status_animal.id_animal,
        alimentacao_saudavel=status_animal.alimentacao_saudavel,
        energia =status_animal.energia,
        forca=status_animal.forca,
        resistencia =status_animal.resistencia,
        felicidade =status_animal.felicidade
    )
    db.add(db_status_animal)
    db.commit()
    db.refresh(db_status_animal)
    return db_status_animal


def update_status_animal(db: Session, status_animal_id: int, status_animal_update: schemas.StatusAnimalUpdate):
    db_status_animal = get_status_animal(db, status_animal_id)
    if not db_status_animal:
        return None
    for field, value in status_animal_update.model_dump(exclude_unset=True).items():
        if field not in ("id", "id_status", "id_animal"):
            setattr(db_status_animal, field, value)

    db.commit()
    db.refresh(db_status_animal)
    return db_status_animal


def delete_status_animal(db: Session, status_animal_id: int):
    db_status_animal = get_status_animal(db, status_animal_id)
    if not db_status_animal:
        return None
    db.delete(db_status_animal)
    db.commit()
    return db_status_animal
