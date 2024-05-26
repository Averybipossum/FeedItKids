from pydantic import BaseModel
from typing import List, Optional

class AnimalBase(BaseModel):
    pass

class AnimalUpdate(AnimalBase):
    id_animal: int

class AnimalResponse(AnimalBase):
    id_animal: int

    class Config:
        orm= True