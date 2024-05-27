from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.database.database  import Base

class StatusAlimento(Base):
    __tablename__ = "alimento_status"

    id_status_alimento = Column(Integer, primary_key=True, autoincrement=True)
    grupo_alimento = Column(String(32), index = True)
    alimentacao_saudavel = Column(Float)
    energia = Column(Float, default=0)
    forca = Column(Float, default=0)
    resistencia = Column(Float, default=0)
    felicidade = Column(Float, default=0)

    consumos_animais = relationship("ConsumoAnimal")