from pydantic import BaseModel

class DisciplinaBase(BaseModel):
    nome: str
    codigo: str

class DisciplinaCreate(DisciplinaBase):
    pass

class DisciplinaOut(DisciplinaBase):
    id: int

    class Config:
        orm_mode = True
