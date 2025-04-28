from pydantic import BaseModel

class HorarioBase(BaseModel):
    dia_semana: str
    horario: str
    turma_id: int

class HorarioCreate(HorarioBase):
    pass

class Horario(HorarioBase):
    id: int
    class Config:
        from_attributes = True 