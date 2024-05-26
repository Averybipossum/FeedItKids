from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database.database import Base

class Usuario(Base):
  __tablename__ = "usuarios"

  id_usuario = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String(128), nullable=False, unique=True)
  hashed_password = Column(String, unique=True)
  id_animal = Column(Integer, ForeignKey("animal.id_animal" ))
  pontuacao_total = Column(Integer, default=0)

  animal = relationship("Animal", back_populates="usuario")
  # ObjetivosCompletos relationship with cascade for delete
  objetivos_completos = relationship("ObjetivoCompleto")
  consumos_animais = relationship("ConsumoAnimal")
