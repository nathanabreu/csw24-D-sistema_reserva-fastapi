from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Turma(Base):
    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
