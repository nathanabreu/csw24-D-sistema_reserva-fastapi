from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.disciplina import Disciplina
from app.schemas.disciplina import DisciplinaCreate, DisciplinaOut
from typing import List

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[DisciplinaOut])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(Disciplina).all()

@router.post("/", response_model=DisciplinaOut)
def criar_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    nova = Disciplina(**disciplina.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
