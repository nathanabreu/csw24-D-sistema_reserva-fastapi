from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.turmas_alunos import turmas_alunos
from app.models.usuarios_grupos import usuarios_grupos
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    primeiro_nome = Column(String, nullable=False)
    ultimo_nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # professor, aluno, etc.
    senha_hash = Column(String, nullable=False)

    turmas = relationship("Turma", secondary=turmas_alunos, back_populates="alunos")
    grupos = relationship("Grupo", secondary=usuarios_grupos, back_populates="usuarios")

    def verificar_senha(self, senha: str) -> bool:
        return pwd_context.verify(senha, self.senha_hash)

    @staticmethod
    def gerar_hash_senha(senha: str) -> str:
        return pwd_context.hash(senha)
