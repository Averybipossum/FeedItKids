from pydantic import BaseModel
from typing import Optional

class ObjetivoCompletoBase(BaseModel):
    id_usuario: int
    id_objetivo: int

class ObjetivoCompletoUpdate(ObjetivoCompletoBase):
    id_usuario: Optional[int] = None  # Optional for updates
    id_objetivo: Optional[int] = None  # Optional for updates

class ObjetivoCompleto(ObjetivoCompletoBase):
    class Config:
        orm = True
