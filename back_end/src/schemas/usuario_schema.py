from pydantic import BaseModel
from typing import Optional
import re

# Pydantic Models

class Token(BaseModel):
    acess_token: str
    token_type: str

    class Config:
        orm = True

class TokenData(BaseModel):
    email: Optional[str] = None
    id_usuario: Optional[int] = None

    class Config:
        orm: True

class UsuarioBase(BaseModel):
    email: str
    pontuacao_total: int

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int


    class Config:
        orm_mode = True


