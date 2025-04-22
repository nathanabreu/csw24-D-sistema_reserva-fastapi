from pydantic import BaseModel

class TurmaBase(BaseModel):
    codigo: str
    disciplina_id: int

class TurmaCreate(TurmaBase):
    pass

class TurmaOut(TurmaBase):
    id: int

    class Config:
        orm_mode = True
