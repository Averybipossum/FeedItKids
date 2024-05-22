from sqlalchemy import Column, Integer, String, Float
from ..database.database import Base

class StatusAlimento(Base):
    __tablename__ = "alimento_status"

    id_status_alimento = Column(Integer, primary_key=True)
    grupo_alimento = Column(String(32))
    alimentacao_saudavel = Column(Float)
    energia = Column(Float)
    forca = Column(Float)
    resistencia = Column(Float)
    felicidade = Column(Float)