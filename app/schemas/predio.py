from pydantic import BaseModel
from typing import Optional

class PredioBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class PredioCreate(PredioBase):
    pass

class Predio(PredioBase):
    id: int

    class Config:
        from_attributes = True 