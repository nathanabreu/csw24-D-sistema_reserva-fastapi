from pydantic import BaseModel

class GrupoBase(BaseModel):
    nome: str

class GrupoCreate(GrupoBase):
    pass

class Grupo(GrupoBase):
    id: int
    class Config:
        from_attributes = True 