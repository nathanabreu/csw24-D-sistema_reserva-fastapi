from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    dia_semana = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    turma_id = Column(Integer, ForeignKey("turmas.id"), nullable=False)

    turma = relationship("Turma", back_populates="horarios") 