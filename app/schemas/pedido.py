from pydantic import BaseModel

class PedidoBase(BaseModel):
    nome: str
    moderador_id: int
    sala_id: int
    recurso_id: int
    status: str

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    class Config:
        from_attributes = True 