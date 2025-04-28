from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.usuario import Usuario
from app.models.horario import Horario
from app.models.turmas_alunos import turmas_alunos

class Turma(Base):
    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    semestre = Column(String, nullable=False)
    professor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    vagas = Column(Integer, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))

    professor = relationship("Usuario", foreign_keys=[professor_id])
    alunos = relationship("Usuario", secondary=turmas_alunos, back_populates="turmas")
    horarios = relationship("Horario", back_populates="turma")
