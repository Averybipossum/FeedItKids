from pydantic import BaseModel
from typing import List, Optional

class AnimalBase(BaseModel):
    id_animal: int
    
    class Config:
        orm= True