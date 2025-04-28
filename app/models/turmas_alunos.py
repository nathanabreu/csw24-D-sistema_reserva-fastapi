from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.session import Base

turmas_alunos = Table(
    "turmas_alunos",
    Base.metadata,
    Column("turma_id", Integer, ForeignKey("turmas.id"), primary_key=True),
    Column("usuario_id", Integer, ForeignKey("usuarios.id"), primary_key=True)
) 