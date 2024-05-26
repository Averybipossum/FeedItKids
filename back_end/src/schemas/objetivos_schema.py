from pydantic import BaseModel
from typing import List, Optional

class ObjetivosBase(BaseModel):
    id_objetivo: int
    descricao: str
    pontuacao: int
    status: str

class ObjetivosUpdate(ObjetivosBase):
    descricao:  Optional[str] = None
    pontuacao:  Optional[str] = None
    status:  Optional[str] = None

class Objetivos(ObjetivosBase):
    id_objetivo: int

    class Config:
         orm= True

