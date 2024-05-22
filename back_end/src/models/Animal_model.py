from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..database.database import Base
from .mixins import Timestamp 

class Animal(Base):
    __tablename__ = "animal"

    id_animal = Column(Integer, primary_key=True)
    nome = Column(String(32), nullable=False)

    usuario = relationship("Usuario", back_populates="animal")
    status_animais = relationship("StatusAnimal", back_populates="animal")

class ConsumoAnimal(Timestamp, Base):
    __tablename__ = "consumo_animal"

    id_consumo = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_status_alimento = Column(Integer, ForeignKey("alimento_status.id_status_alimento"))
    alimento = Column(String(64))

    usuario = relationship("Usuario", back_populates="consumos_animais")
    status_alimento = relationship("StatusAlimento", back_populates="consumos_animais")

class StatusAnimal(Timestamp, Base):
    __tablename__ = "status_animal"

    id_status_animal = Column(Integer, primary_key=True)
    status = Column(Integer, ForeignKey("alimento_status.id_status_alimento"))
    id_animal = Column(Integer, ForeignKey("animal.id_animal"))

    animal = relationship("Animal", back_populates="status_animais")
    status_alimento = relationship("StatusAlimento", back_populates="status_animais")