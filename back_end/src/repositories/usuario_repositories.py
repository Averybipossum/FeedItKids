from sqlalchemy.orm import Session
from psycopg2 import DataError, IntegrityError, OperationalError
from src.models import Usuario_model as models
from src.models import Animal_model
from src.schemas import usuario_schema as schemas
from src.schemas import animal_schema
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from datetime import timedelta, datetime
from typing import Annotated
import pytz

# Inicializações necessárias
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
utc_timezone = pytz.utc
SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'

# CRUD USUARIO BANCO DE DADOS
def get_usuario(db: Session, id_usuario: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    try:
        db_usuario = models.Usuario(
            email=usuario.email,
            hashed_password=bcrypt_context.hash(usuario.senha),
            id_animal=usuario.id_animal,
            pontuacao_total=usuario.pontuacao_total
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except (IntegrityError, DataError) as e:
        raise Exception(f"Error creating user: {str(e)}") from e
    except OperationalError as e:
        raise Exception(f"Database error: {str(e)}") from e
def delete_usuario(db: Session, id_usuario: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return None

# Autentificação
def authenticate_user(email: str, senha: str, db: Session):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not db_usuario:
        return False
    if not bcrypt_context.verify(senha, db_usuario.hashed_password):
        return False
    return db_usuario

def create_acess_token(email: str, id_usuario: int, expires_delta: timedelta):
    encode = {'sub': email, 'id': id_usuario}
    expires = datetime.now(utc_timezone) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        id_usuario: int = payload.get('id')
        if email is None or id_usuario is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user.')
        return {'email': email, 'id_usuario': id_usuario}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user')


# função cadastro usuário + criar animal

def create_user_and_animal(db: Session, user: schemas.UsuarioCreate, animal: animal_schema.AnimalBase):
    try:
        # Crie o animal
        db_animal = Animal_model.Animal()
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)
        
        # Use o ID do animal recém-criado para criar o usuário com a referência correta para o animal
        db_user = models.Usuario(
            email=user.email,
            hashed_password=bcrypt_context.hash(user.senha),
            id_animal=db_animal.id_animal,  # Use o ID do animal recém-criado
            pontuacao_total=user.pontuacao_total
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise Exception(f"Error creating user and animal: {str(e)}") from e
    except OperationalError as e:
        db.rollback()
        raise Exception(f"Database error: {str(e)}") from e