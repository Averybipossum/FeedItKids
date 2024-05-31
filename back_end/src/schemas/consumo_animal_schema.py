from pydantic import BaseModel, EmailStr

class ConsumoAnimalBase(BaseModel):
    id_usuario: int 
    id_status_alimento: int
    alimento: str

class ConsumoAnimal(ConsumoAnimalBase):
    id_consumo: int

    class Config:
        orm_mode = True
