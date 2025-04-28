from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.session import Base

usuarios_grupos = Table(
    "usuarios_grupos",
    Base.metadata,
    Column("usuario_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("grupo_id", Integer, ForeignKey("grupos.id"), primary_key=True)
) 