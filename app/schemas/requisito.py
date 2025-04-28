from pydantic import BaseModel

class RequisitoBase(BaseModel):
    tipo: str
    disciplina_id: int

class RequisitoCreate(RequisitoBase):
    pass

class Requisito(RequisitoBase):
    id: int
    class Config:
        from_attributes = True 