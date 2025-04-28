from sqlalchemy import Column, Integer, String
from app.db.session import Base

class TipoRecurso(Base):
    __tablename__ = "tipos_recurso"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False) 