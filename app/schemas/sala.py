from pydantic import BaseModel

class SalaBase(BaseModel):
    numero: str
    capacidade: int
    andar: int
    predio_id: int

class SalaCreate(SalaBase):
    pass

class Sala(SalaBase):
    id: int
    class Config:
        from_attributes = True
