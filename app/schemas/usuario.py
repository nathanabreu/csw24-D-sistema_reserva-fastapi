from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    username: str
    primeiro_nome: str
    ultimo_nome: str
    tipo: str
    grupos_ids: list[int] = []

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        from_attributes = True
