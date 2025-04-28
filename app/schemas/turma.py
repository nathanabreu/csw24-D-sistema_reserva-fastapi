from pydantic import BaseModel

class TurmaBase(BaseModel):
    numero: str
    semestre: str
    professor_id: int
    vagas: int
    disciplina_id: int

class TurmaCreate(TurmaBase):
    alunos_ids: list[int] = []
    horarios_ids: list[int] = []

class Turma(TurmaBase):
    id: int
    alunos_ids: list[int] = []
    horarios_ids: list[int] = []
    class Config:
        from_attributes = True
