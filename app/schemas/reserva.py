from enum import Enum
from datetime import datetime
from pydantic import BaseModel

class StatusEnum(str, Enum):
    PENDENTE = "pendente"
    APROVADA = "aprovada"
    REJEITADA = "rejeitada"

class ReservaBase(BaseModel):
    data_criacao: datetime
    data_validade: datetime
    observacao: str | None = None
    status: StatusEnum
    usuario_id: int
    recurso_id: int
    aula_id: int | None = None

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int
    class Config:
        from_attributes = True
