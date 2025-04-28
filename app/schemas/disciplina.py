from pydantic import BaseModel

class DisciplinaBase(BaseModel):
    nome: str
    codigo: str
    creditos: int
    ementa: str

class DisciplinaCreate(DisciplinaBase):
    pass

class Disciplina(DisciplinaBase):
    id: int
    class Config:
        from_attributes = True
