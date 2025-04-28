from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from app.db.session import Base
import enum

class StatusEnum(enum.Enum):
    PENDENTE = "pendente"
    APROVADA = "aprovada"
    REJEITADA = "rejeitada"

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    data_criacao = Column(DateTime, nullable=False)
    data_validade = Column(DateTime, nullable=False)
    observacao = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    recurso_id = Column(Integer, ForeignKey("recursos.id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=True)
