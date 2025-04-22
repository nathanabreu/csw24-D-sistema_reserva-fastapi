from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.reserva import Reserva
from app.schemas.reserva import ReservaCreate, ReservaOut
from typing import List

router = APIRouter(prefix="/reservas", tags=["Reservas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()

@router.post("/", response_model=ReservaOut)
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    nova = Reserva(**reserva.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
