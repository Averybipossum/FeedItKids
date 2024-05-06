from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from db_setup import Base


class Animal(Base):
    __tablename__ = "animal"

    id_animal = Column(Integer, primary_key=True)
    nome = Column(String(32), nullable=False)

    usuario = relationship("usuario", back_populates="animal")

class ConsumoAnimal(Base):
    __tablename__ = "consumo_Animal"

    id_consumo = Column(Integer, primary_key=True)
    id_usuario = Column(EmailType, ForeignKey("usuarios.id_usuario"))
    grupo_alimento = Column(String(32), ForeignKey("alimento.grupo_alimento"))
    alimento = Column(String(64))
    qtd_consumo = Column(Integer)
    data_consumo = Column(Date)

    usuario = relationship("Usuarios", back_populates="consumo_Animal")
    grupoAlimento = relationship("Alimento", back_populates="consumo_Animal")