from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..config import senha

SQLALCHEMY_DATABASE_URL = f"postgres://avnadmin:{senha}@pg-25cb39a-abnschlink-031a.h.aivencloud.com:22352/db_fitKids"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future= True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()