from pydantic import BaseModel

class PredioBase(BaseModel):
    numero: str
    nome: str
    rua: str
    numero_endereco: str
    complemento: str | None = None
    bairro: str
    cidade: str
    uf: str
    cep: str

class PredioCreate(PredioBase):
    pass

class Predio(PredioBase):
    id: int
    class Config:
        from_attributes = True 