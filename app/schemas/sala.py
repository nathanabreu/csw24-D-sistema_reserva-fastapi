from pydantic import BaseModel

class SalaBase(BaseModel):
    nome: str
    capacidade: int

class SalaCreate(SalaBase):
    pass

class SalaOut(SalaBase):
    id: int

    class Config:
        orm_mode = True
