from typing import List

from requests import Session
from src.database.database import get_db
from src.repositories import objetivos_repositories as crud
from fastapi import APIRouter, Depends, HTTPException
from src.models.Objetivo_model import Objetivos
from src.schemas import objetivos_schema as schemas


router = APIRouter()

# Fila de requisição de objetivos

class No:
    def __init__(self, info):
        self.info = info
        self.proximo = None

# Funções da fila 
class FilaObjetivos:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def esta_vazia(self):
        return self.primeiro is None

    def enfileira(self, objetivo):
        novo = No(objetivo)
        if self.esta_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def desenfileira(self):
        if self.esta_vazia():
            return None
        temp = self.primeiro.info
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        return temp

fila_objetivos = FilaObjetivos()

@router.post("/objetivos/")
async def adicionar_objetivo(objetivo: schemas.Objetivos, db: Session = Depends(get_db)):
    # novo objetivo (get_Objetivo_db)
    novo_objetivo = crud.create_objetivos(db, objetivo)
    fila_objetivos.enfileira(novo_objetivo)
    return {"message": "Objetivo adicionado com sucesso!"}

@router.get("/objetivos/")
async def obter_fila_objetivos():
    fila_lista = []
    no_atual = fila_objetivos.primeiro
    while no_atual is not None:
        fila_lista.append(no_atual.info)
        no_atual = no_atual.proximo
    return fila_lista

@router.delete("/objetivos/")
async def remover_objetivo(db: Session = Depends(get_db)):
    objetivo_removido = fila_objetivos.desenfileira()
    if objetivo_removido:
        crud.update_objetivo_status(db, objetivo_removido.id_objetivo, status=True)
        return {"message": "Objetivo removido com sucesso!", "objetivo": objetivo_removido}
    else:
        raise HTTPException(status_code=404, detail="Fila de objetivos vazia!")

