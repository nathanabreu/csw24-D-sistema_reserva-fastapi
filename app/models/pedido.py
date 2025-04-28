from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    moderador_id = Column(Integer, ForeignKey("usuarios.id"))
    sala_id = Column(Integer, ForeignKey("salas.id"))
    recurso_id = Column(Integer, ForeignKey("recursos.id"))
    status = Column(String, nullable=False) 