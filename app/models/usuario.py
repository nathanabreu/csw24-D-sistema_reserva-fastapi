from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    tipo = Column(String, nullable=False)  # admin, coordenador, professor, aluno
