from sqlalchemy import func
from sqlalchemy.orm import Session
from src.models import Animal_model as models 
from src.schemas import status_animal_schema as schemas
from src.models import status_alimento_model

# CRUD BANCO DE DADOS


def get_status_animal(db: Session, id_animal: int):
    return db.query(models.StatusAnimal).filter(models.StatusAnimal.id_animal == id_animal).first()


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
        return {"message": "StatusAnimal not found"}
    db.delete(db_status_animal)
    db.commit()
    return {"message": "StatusAnimal deleted successfully"}



def encontrar_animal_por_alimento(db: Session, alimento_id):
    # Primeiro, vamos encontrar o id do animal através da tabela de consumo
    consumo = db.query(models.ConsumoAnimal).filter(models.ConsumoAnimal.id_status_alimento == alimento_id).first()
    
    if consumo:
        # Agora, podemos usar o id do animal encontrado para obter o animal correspondente
        animal = db.query(models.StatusAnimal).filter(models.StatusAnimal.id_animal == consumo.id_status_alimento).first()
        
        return animal
    
    return None

# Soma Status + Status Animal
def soma_status_animal(db:Session):
    # Consulta od dados da tabela alimentos_status
    alimentos = db.query(status_alimento_model).all()

    # Para cada linha na tabela linha status
    for alimento in alimentos:

        # Consulta a linha correspondente na tabela status_alimento
        id_status_alimento = alimento.id_status_alimento
        animal = encontrar_animal_por_alimento(db, alimento.id_status_alimento)

        if animal:
            # Somar os valores dos atributos da tabela alimento_status aos valores correspondentes na tabela status_animal
            animal.alimentacao_saudavel = min(animal.alimentacao_saudavel + alimento.alimentacao_saudavel, 10)
            animal.energia = min(animal.energia + alimento.energia, 10)
            animal.forca = min(animal.forca + alimento.forca, 10)
            animal.resistencia = min(animal.resistencia + alimento.resistencia, 10)
            animal.felicidade = min(animal.felicidade + alimento.felicidade, 10)

            # Atualizar os valores na tabela status_animal
            db.commit()

        


