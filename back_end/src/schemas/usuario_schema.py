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
    senha:str
    id_animal: Optional[int] = None
    pontuacao: int

class UsuarioUpdate(UsuarioBase):
    pontuacao: Optional[int]


class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        orm = True



