from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.reserva import Reserva as ReservaModel
from app.schemas.reserva import Reserva, ReservaCreate
from app.db.session import get_db
from app.models.usuario import Usuario as UsuarioModel
from app.core.permissions import checar_permissao

router = APIRouter(tags=["Reservas"])

@router.post("/reservas/", response_model=Reserva)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == reserva.usuario_id).first()
    checar_permissao(usuario, "professor")
    db_reserva = ReservaModel(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

@router.get("/reservas/{reserva_id}", response_model=Reserva)
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    return db.query(ReservaModel).filter(ReservaModel.id == reserva_id).first()

@router.get("/reservas/", response_model=list[Reserva])
def read_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ReservaModel).offset(skip).limit(limit).all()

@router.delete("/reservas/{reserva_id}")
def delete_reserva(reserva_id: int, db: Session = Depends(get_db)):
    db_reserva = db.query(ReservaModel).filter(ReservaModel.id == reserva_id).first()
    if db_reserva is None:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    db.delete(db_reserva)
    db.commit()
    return {"ok": True} 