from pydantic import BaseModel
from typing import List, Optional

class ObjetivosBase(BaseModel):
    descricao: Optional [str] = None
    pontuacao: Optional [int] = None

class ObjetivosCreate(ObjetivosBase):
    ...

class ObjetivosUpdate(ObjetivosBase):
    ... 

class Objetivos(ObjetivosBase):
    id_objetivo: int

    class Config:
         orm= True

