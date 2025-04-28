from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    capacidade = Column(Integer)
    andar = Column(Integer, nullable=False)
    predio_id = Column(Integer, ForeignKey("predios.id"), nullable=False)
