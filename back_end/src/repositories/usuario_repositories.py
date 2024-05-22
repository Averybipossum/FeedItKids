from psycopg2 import DataError, IntegrityError, OperationalError
from sqlalchemy.orm import Session
from src.models import usuario_model as models
from ..schemas import usuario_schema as schemas
import bcrypt
# CRUD USUARIO BANCO DE DADOS 


def get_usuario(db: Session, id_usuario: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Usuario).offset(skip).limit(limit).all()
    
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_senha = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())

    try:
        db_usuario = models.Usuario(
            email=usuario.email_usuario,
            nome=usuario.nome,
            papel=usuario.papel,
            id_animal=usuario.id_animal,
            senha=hashed_senha.decode('utf-8')
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except (IntegrityError, DataError) as e:
        raise Exception(f"Error creating user: {str(e)}") from e
    except OperationalError as e:
        raise Exception(f"Database error: {str(e)}") from e


def update_usuario(db: Session, id_usuario: int, usuario: schemas.UsuarioUpdate):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if usuario.senha:
        hashed_senha = bcrypt.hashpw(usuario.senha, bcrypt.gensalt())
        db_usuario.senha = hashed_senha.decode('utf-8')
        for key, value in usuario.__dict__.items():
            if key not in ('senha', 'id_usuario'):
                setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, id_usuario: str):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return None 