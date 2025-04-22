from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.turma import Turma
from app.schemas.turma import TurmaCreate, TurmaOut
from typing import List

router = APIRouter(prefix="/turmas", tags=["Turmas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TurmaOut])
def listar_turmas(db: Session = Depends(get_db)):
    return db.query(Turma).all()

@router.post("/", response_model=TurmaOut)
def criar_turma(turma: TurmaCreate, db: Session = Depends(get_db)):
    nova = Turma(**turma.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
