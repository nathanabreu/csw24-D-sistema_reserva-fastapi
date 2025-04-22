from pydantic import BaseModel
from datetime import datetime

class ReservaBase(BaseModel):
    usuario_id: int
    sala_id: int
    horario_inicio: datetime
    horario_fim: datetime

class ReservaCreate(ReservaBase):
    pass

class ReservaOut(ReservaBase):
    id: int

    class Config:
        orm_mode = True
