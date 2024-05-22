from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..database.database import Base

class Usuario(Base):
  __tablename__ = "usuarios"

  id_usuario = Column(Integer, primary_key=True)
  email_usuario = Column(String(128), nullable=False, unique=True)
  nome = Column(String(64), nullable=False)
  senha = Column(String(128), nullable=False)
  papel = Column(String(32), nullable=False)
  id_animal = Column(Integer, ForeignKey("animal.id_animal"))

  animal = relationship("Animal", back_populates="usuario")
  # ObjetivosCompletos relationship with cascade for delete
  objetivos_completos = relationship("ObjetivoCompleto", backref="usuario", cascade="delete, delete-orphan")
  consumos_animais = relationship("ConsumoAnimal", back_populates="usuario")

  pontuacao_total = Column(Integer, default=0)