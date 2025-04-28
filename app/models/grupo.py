from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.usuarios_grupos import usuarios_grupos

class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    usuarios = relationship("Usuario", secondary=usuarios_grupos, back_populates="grupos") 