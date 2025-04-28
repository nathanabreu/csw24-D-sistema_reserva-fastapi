from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from app.db.session import Base

class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    data = Column(DateTime, nullable=False)
    sala_id = Column(Integer, ForeignKey("salas.id"))
    conteudo = Column(String, nullable=True) 