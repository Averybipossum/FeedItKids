from pydantic import BaseModel
from typing import Optional

class StatusBase(BaseModel):
    grupoAlimento: str
    alimentacaoSaudavel: float  
    energia: float
    forca: float
    resistencia: float
    felicidade: float

class StatusResponse(StatusBase):
    id_status_alimento: int
    grupo_alimento: str

    class Config:
        orm = True
