from sqlalchemy.orm import Session
from src.models import animal_model as models
from ..schemas import consumo_animal_schema as schemas


# CRUD BANCO DE DADOS 


def get_consumo(db: Session, id_consumo: int):
    return db.query(models.ConsumoAnimal).filter(models.ConsumoAnimal.id_consumo == id_consumo).first()

def get_consumos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ConsumoAnimal).offset(skip).limit(limit).all()

def create_consumo(db: Session, consumo_animal: schemas.ConsumoAnimalCreate):
    db_consumo_animal = models.ConsumoAnimal(
        id_usuario = consumo_animal.id_usuario,
        grupo_alimento = consumo_animal.grupo_alimento,
        alimento = consumo_animal.alimento,
        qtd_consumo = consumo_animal.qtd_consumo)
    db.add(db_consumo_animal)
    db.commit()
    db.refresh(db_consumo_animal)
    return db_consumo_animal

def update_consumo(db: Session, id_consumo: int, consumo_update: schemas.ConsumoAnimalCreate) -> models.ConsumoAnimal:
    db_consumo_animal = db.query(models.ConsumoAnimal).filter(models.ConsumoAnimal.id_consumo == id_consumo).first()

    if not db_consumo_animal:
        return None

    for field, value in consumo_update.dict(exclude_unset=True).items():
        setattr(db_consumo_animal, field, value)

    db.commit()
    db.refresh(db_consumo_animal)
    return db_consumo_animal


def delete_consumo_animal(db: Session, id_consumo: int):
    db_consumo_animal = get_consumo(db, id_consumo)
    if not db_consumo_animal:
        return None
    db.delete(db_consumo_animal)
    db.commit()
    return db_consumo_animal