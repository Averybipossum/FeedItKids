from pydantic import BaseModel

class StatusAnimalBase(BaseModel):
    id_status: int
    id_animal: int

class StatusAnimalCreate(StatusAnimalBase):
    pass

class StatusAnimal(StatusAnimalBase):
    id: int

    class Config:
        orm= True
