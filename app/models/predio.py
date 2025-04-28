from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Predio(Base):
    __tablename__ = "predios"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    numero_endereco = Column(String, nullable=False)
    complemento = Column(String, nullable=True)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    cep = Column(String, nullable=False) 