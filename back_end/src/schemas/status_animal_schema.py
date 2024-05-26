from typing import Optional
from pydantic import BaseModel

class StatusAnimalBase(BaseModel):
    grupo_alimento: str
    alimentacao_saudavel:float
    energia :float
    forca:float
    resistencia :float
    felicidade :float
    
class StatusAnimalUpdate(StatusAnimalBase):
    grupo_alimento: Optional[str]
    alimentacao_saudavel:Optional[float]
    energia :Optional[float]
    forca:Optional[float]
    resistencia :Optional[float]
    felicidade :Optional[float]
    

class StatusAnimal(StatusAnimalBase):
    id_status_alimento: int

    class Config:
        orm= True
