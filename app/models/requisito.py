from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Requisito(Base):
    __tablename__ = "requisitos"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False) 