from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    tipo: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
