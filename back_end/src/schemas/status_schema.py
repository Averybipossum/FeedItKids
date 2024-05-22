from pydantic import BaseModel
from typing import Optional

class StatusBase(BaseModel):
    alimentacaoSaudavel: float  
    energia: float
    forca: float
    resistencia: float
    felicidade: float
    grupoAlimento: Optional[str]

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    grupo_alimento: str

    class Config:
        orm = True
