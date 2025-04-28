from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    creditos = Column(Integer, nullable=False)
    ementa = Column(String, nullable=False)
