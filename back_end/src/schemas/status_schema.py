from pydantic import BaseModel

class StatusBase(BaseModel):
    grupo_alimento: str
    alimentacao_saudavel: float  
    energia: float
    forca: float
    resistencia: float
    felicidade: float

class StatusResponse(StatusBase):
    id_status_alimento: int

    class Config:
        from_attributes = True
