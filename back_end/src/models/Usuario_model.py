from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from db_setup import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(EmailType, primary_key=True)
    nome = Column(String(64), nullable=False)
    senha = Column(String(128), nullable=False)
    papel = Column(String(32), nullable=False)
    id_animal = Column(Integer, ForeignKey("animal.id_animal"))

    animal = relationship("Animal", back_populates="usuario")

    objetivo_completo = relationship("ObejtivoCompleto", secondary="usuarios")
