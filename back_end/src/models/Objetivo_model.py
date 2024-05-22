from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database.database import Base

class Objetivos(Base):
    __tablename__ = "objetivos"

    id_objetivo = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    pontuacao = Column(Integer, nullable=False)

class ObjetivoCompleto(Base):
    __tablename__ = "objetivo_completo"

    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    id_objetivo = Column(Integer, ForeignKey("objetivos.id_objetivo"), primary_key=True)
    pontuacao = Column(Integer, nullable=False)

    usuario = relationship("Usuario", back_populates="objetivo_completo")
    objetivo = relationship("Objetivos", back_populates="objetivo_completos")