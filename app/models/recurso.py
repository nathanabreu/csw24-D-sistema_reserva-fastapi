from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.session import Base

class Recurso(Base):
    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    status = Column(String, nullable=False)
    disponivel = Column(Boolean, default=True)
    tipo_recurso_id = Column(Integer, ForeignKey("tipos_recurso.id")) 