from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pedido import Pedido, PedidoCreate
from app.models.pedido import Pedido as PedidoModel
from app.db.session import get_db
from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel

router = APIRouter()

@router.post("/pedidos/", response_model=Pedido)
def create_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == pedido.moderador_id).first()
    checar_permissao(usuario, "admin")
    db_pedido = PedidoModel(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

@router.get("/pedidos/{pedido_id}", response_model=Pedido)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    return db.query(PedidoModel).filter(PedidoModel.id == pedido_id).first()

@router.get("/pedidos/", response_model=list[Pedido])
def read_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(PedidoModel).offset(skip).limit(limit).all()

@router.delete("/pedidos/{pedido_id}")
def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = db.query(PedidoModel).filter(PedidoModel.id == pedido_id).first()
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db.delete(db_pedido)
    db.commit()
    return {"ok": True} 