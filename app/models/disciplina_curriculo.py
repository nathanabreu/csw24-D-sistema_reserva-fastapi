from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.session import Base

class DisciplinaCurriculo(Base):
    __tablename__ = "disciplinas_curriculo"

    id = Column(Integer, primary_key=True, index=True)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
    curriculo_id = Column(Integer, ForeignKey("curriculos.id"), nullable=False)
    semestre = Column(String, nullable=False) 