from psycopg2 import IntegrityError, OperationalError
from sqlalchemy import func
from sqlalchemy.orm import Session
from src.models import Animal_model as models
from src.models import status_alimento_model
from src.schemas import status_animal_schema as schemas

# CRUD BANCO DE DADOS


def get_status_animal(db: Session, id_usuario: int):
    return db.query(models.StatusAnimal).filter(models.StatusAnimal.id_usuario == id_usuario).first()


def get_status_animals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StatusAnimal).offset(skip).limit(limit).all()

def create_status_animal(db: Session, status_animal: schemas.StatusAnimalBase):

    db_status_animal = models.StatusAnimal(
        id_usuario = status_animal.id_usuario,
        alimentacao_saudavel=status_animal.alimentacao_saudavel,
        energia =status_animal.energia,
        forca=status_animal.forca,
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
        if field not in ("id", "id_status", "id_usuario"):
            setattr(db_status_animal, field, value)

    db.commit()
    db.refresh(db_status_animal)
    return db_status_animal


def delete_status_animal(db: Session, status_animal_id: int):
    db_status_animal = get_status_animal(db, status_animal_id)
    if not db_status_animal:
        return {"message": "StatusAnimal not found"}
    db.delete(db_status_animal)
    db.commit()
    return {"message": "StatusAnimal deleted successfully"}



# Função para encontrar o animal correspondente ao alimento
def encontrar_animal_por_alimento(db: Session, alimento_id):
    consumo = db.query(models.ConsumoAnimal).filter(models.ConsumoAnimal.id_status_alimento == alimento_id).first()
    if consumo:
        animal = db.query(models.StatusAnimal).filter(models.StatusAnimal.id_usuario == consumo.id_status_alimento).first()
        return animal
    return None

# Função para transferir e somar os valores de alimento_status para status_animal
def transferir_e_somar_valores(db: Session, grupo_alimento: str, id_usuario: int):
    try:
        # Buscar o alimento correspondente ao grupo_alimento
        alimento = db.query(status_alimento_model.StatusAlimento).filter(
            status_alimento_model.StatusAlimento.grupo_alimento.ilike(f"%{grupo_alimento}%")
        ).first()

        if alimento:
            # Encontrar o animal correspondente ao alimento
            animal = encontrar_animal_por_alimento(db, alimento.id_status_alimento)

            if animal:
                # Somar os valores dos atributos da tabela alimento_status aos valores correspondentes na tabela status_animal
                animal.alimentacao_saudavel = min(animal.alimentacao_saudavel + alimento.alimentacao_saudavel, 10)
                animal.energia = min(animal.energia + alimento.energia, 10)
                animal.forca = min(animal.forca + alimento.forca, 10)
                animal.felicidade = min(animal.felicidade + alimento.felicidade, 10)

                # Atualizar os valores na tabela status_animal
                db.commit()
                return animal
            else:
                raise Exception("Animal correspondente ao alimento não encontrado.")
        else:
            raise Exception("Alimento correspondente ao grupo não encontrado.")
    except (IntegrityError, OperationalError) as e:
        db.rollback()
        raise Exception(f"Erro ao transferir e somar valores: {str(e)}") from e
