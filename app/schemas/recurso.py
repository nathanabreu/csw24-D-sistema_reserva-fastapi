from pydantic import BaseModel

class RecursoBase(BaseModel):
    descricao: str
    status: str
    disponivel: bool
    tipo_recurso_id: int

class RecursoCreate(RecursoBase):
    pass

class Recurso(RecursoBase):
    id: int
    class Config:
        from_attributes = True 