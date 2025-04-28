from pydantic import BaseModel
from datetime import datetime

class AulaBase(BaseModel):
    turma_id: int
    data: datetime
    sala_id: int
    conteudo: str | None = None

class AulaCreate(AulaBase):
    pass

class Aula(AulaBase):
    id: int
    class Config:
        from_attributes = True 