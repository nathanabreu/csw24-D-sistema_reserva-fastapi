from pydantic import BaseModel

class DisciplinaCurriculoBase(BaseModel):
    disciplina_id: int
    curriculo_id: int
    semestre: str

class DisciplinaCurriculoCreate(DisciplinaCurriculoBase):
    pass

class DisciplinaCurriculo(DisciplinaCurriculoBase):
    id: int
    class Config:
        from_attributes = True 