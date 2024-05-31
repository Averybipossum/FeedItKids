from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  src.database.database import Base
from .mixins import Timestamp 

class Animal(Base):
    __tablename__ = "animal"
    id_animal = Column(Integer, primary_key=True, autoincrement=True)
    usuario = relationship("Usuario")
    status_animais = relationship("StatusAnimal")

class ConsumoAnimal(Timestamp, Base):
    __tablename__ = "consumo_animal"

    id_consumo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_status_alimento = Column(Integer, ForeignKey("alimento_status.id_status_alimento"))
    alimento = Column(String(255))
    qtd = Column(Float)


    usuario = relationship("Usuario", back_populates="consumos_animais")
    status_alimento = relationship("StatusAlimento", back_populates="consumos_animais")

class StatusAnimal(Timestamp, Base):
    __tablename__ = "status_animal"

    id_status_animal = Column(Integer, primary_key=True, autoincrement=True)
    id_animal = Column(Integer, ForeignKey("animal.id_animal"))
    alimentacao_saudavel = Column(Float, nullable=False)
    energia = Column(Float, nullable=False)
    forca = Column(Float, nullable=False)
    felicidade = Column(Float, nullable=False)

    animal = relationship("Animal", back_populates="status_animais")