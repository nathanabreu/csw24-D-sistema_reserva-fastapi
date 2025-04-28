from pydantic import BaseModel

class TipoRecursoBase(BaseModel):
    nome: str

class TipoRecursoCreate(TipoRecursoBase):
    pass

class TipoRecurso(TipoRecursoBase):
    id: int
    class Config:
        from_attributes = True 