from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Curriculo(Base):
    __tablename__ = "curriculos"

    id = Column(Integer, primary_key=True, index=True)
    nome_curso = Column(String, nullable=False)
    semestre_inicio_vigencia = Column(String, nullable=False)
    semestre_fim_vigencia = Column(String, nullable=False) 