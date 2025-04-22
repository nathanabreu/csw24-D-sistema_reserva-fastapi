from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.sala import Sala
from app.schemas.sala import SalaCreate, SalaOut
from typing import List

router = APIRouter(prefix="/salas", tags=["Salas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[SalaOut])
def listar_salas(db: Session = Depends(get_db)):
    return db.query(Sala).all()

@router.post("/", response_model=SalaOut)
def criar_sala(sala: SalaCreate, db: Session = Depends(get_db)):
    nova = Sala(**sala.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
