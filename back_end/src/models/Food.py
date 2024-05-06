from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from db_setup import Base

class Alimentos(Base):
    __tablename__ = "alimento"

    grupo_alimento = Column(String(32), primary_key=True)


class Status(Base):
    __tablename__ = "status"

    id_status = Column(Integer, primary_key=True)
    alimentacao_saudavel = Column(Integer)
    energia = Column(Integer)
    forca = Column(Integer)
    resistencia = Column(Integer)
    felicidade = Column(Integer)
    grupo_alimento = Column(String(32), ForeignKey("alimentos.grupo_alimento"))

    grupoAlimento = relationship("Alimento", back_populates="status")