from sqlalchemy.orm import Session
from src.models import objetivo_model as models 
from src.schemas import objetivo_completo_schema as schemas

# CRUD objetivos completo


def get_objetivo_completo(db: Session, id_objetivo_completo: int):
    return db.query(models.ObjetivoCompleto).filter(models.ObjetivoCompleto.id_objetivo == id_objetivo_completo).first()


def get_objetivos_completo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ObjetivoCompleto).offset(skip).limit(limit).all()


def create_objetivo_completo(db: Session, objetivo: schemas.ObjetivoCompletoBase):
    db_objetivo_completo = models.ObjetivoCompleto(
        id_objetivo=objetivo.id_objetivo,
        id_usuario=objetivo.id_usuario,
    )
    db.add(db_objetivo_completo)
    db.commit()
    db.refresh(db_objetivo_completo)
    return db_objetivo_completo


def update_objetivo_completo(db: Session, id_objetivo_completo: int, objetivo: schemas.ObjetivoCompletoUpdate):
    db_objetivo_completo = db.query(models.ObjetivoCompleto).filter(models.ObjetivoCompleto.id_objetivo_completo == id_objetivo_completo).first()
    if db_objetivo_completo:
        for key, value in objetivo.model_dump(exclude_unset=True).items():
            setattr(db_objetivo_completo, key, value)
        db.commit()
        db.refresh(db_objetivo_completo)
    return db_objetivo_completo


def delete_objetivo_completo(db: Session, id_objetivo_completo: int):
    db_objetivo_completo = db.query(models.ObjetivoCompleto).filter(models.ObjetivoCompleto.id_objetivo_completo == id_objetivo_completo).first()
    if db_objetivo_completo:
        db.delete(db_objetivo_completo)
        db.commit()
    return None
