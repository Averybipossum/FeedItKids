from pydantic import BaseModel, EmailStr

class ConsumoAnimalBase(BaseModel):
    id_usuario: int  
    grupo_alimento: str
    alimento: str
    qtd_consumo: int

class ConsumoAnimalCreate(ConsumoAnimalBase):
    pass

class ConsumoAnimal(ConsumoAnimalBase):
    id_consumo: int

    class Config:
        orm = True
