from pydantic import BaseModel
from typing import Optional
import re

# Custom Validators (separate functions)
def validate_email(email_usuario):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email_usuario))

def senha_must_be_strong(v):
    if len(v) < 8:
        raise ValueError('A senha deve ter pelo menos 8 caracteres')
    if not re.search("[A-Z]", v):
        raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
    if not re.search("[a-z]", v):
        raise ValueError('A senha deve conter pelo menos uma letra minúscula')
    if not re.search("[0-9]", v):
        raise ValueError('A senha deve conter pelo menos um número')
    if not re.search("[@#$%^&+=]", v):
        raise ValueError('A senha deve conter pelo menos um caractere especial (@#$%^&+=)')
    return v

# Pydantic Models
class UsuarioBase(BaseModel):
    email_usuario: str
    nome: str
    papel: str
    id_animal: Optional[int] = None


class UsuarioCreate(UsuarioBase):
    senha: str 

class UsuarioUpdate(UsuarioBase):
    senha: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        orm = True

