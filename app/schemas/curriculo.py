from pydantic import BaseModel

class CurriculoBase(BaseModel):
    nome_curso: str
    semestre_inicio_vigencia: str
    semestre_fim_vigencia: str

class CurriculoCreate(CurriculoBase):
    pass

class Curriculo(CurriculoBase):
    id: int
    class Config:
        from_attributes = True 