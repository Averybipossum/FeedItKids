from pydantic import BaseModel
from typing import List, Optional

class AnimalBase(BaseModel):
    nome: str

class AnimalUpdate(AnimalBase):
    nome:Optional[str]

class Animal(AnimalBase):
    id_animal: int
    status_animal: Optional[int]
    
    class Config:
        orm= True