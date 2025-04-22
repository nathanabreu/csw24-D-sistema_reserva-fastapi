from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.session import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    sala_id = Column(Integer, ForeignKey("salas.id"))
    horario_inicio = Column(DateTime)
    horario_fim = Column(DateTime)
