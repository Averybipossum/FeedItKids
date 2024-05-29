from pydantic import BaseModel
from typing import Optional
import re

# Pydantic Models

class Token(BaseModel):
    acess_token: str
    token_type: str

    class Config:
        orm = True

class UsuarioBase(BaseModel):
    email: str
    id_animal: int
    pontuacao_total: int

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int


    class Config:
        orm_mode = True


