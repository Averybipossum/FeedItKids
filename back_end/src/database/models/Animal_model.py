import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from back_end.src.database.db_setup import Base

from .mixins import Timestamp

class Animal(Base):
    __tablename__ = "animal"

    id_animal = Column(Integer, primary_key=True)
    nome = Column(String(32), nullable=False)

    usuario = relationship("Usuario", back_populates="Animal")
    status_animal = relationship("StatusAnimal", back_populates="animal")

class ConsumoAnimal(Timestamp,Base):
    __tablename__ = "consumo_Animal"

    id_consumo = Column(Integer, primary_key=True)
    id_usuario = Column(EmailType, ForeignKey("usuarios.id_usuario"))
    grupo_alimento = Column(String(32), ForeignKey("alimento.grupo_alimento"))
    alimento = Column(String(64))
    qtd_consumo = Column(Integer)

    usuario = relationship("Usuario", back_populates="ConsumoAnimal")
    grupoAlimento = relationship("Alimento", back_populates="ConsumoAnimal")

class StatusAnimal(Timestamp,Base):
    __tablename__ = "status_animal"

    id = Column(Integer, primary_key=True)
    id_status = Column(Integer, ForeignKey("status.id_status"))
    id_animal = Column(Integer, ForeignKey("animal.id_animal"))

    animal = relationship("Animal", back_populates="status_animal")
    status = relationship("Satus")

        


