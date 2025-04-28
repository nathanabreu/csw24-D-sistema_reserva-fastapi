from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.turma import Turma as TurmaModel
from app.schemas.turma import Turma, TurmaCreate
from app.db.session import get_db

router = APIRouter(tags=["Turmas"])

@router.post("/turmas/", response_model=Turma)
def create_turma(turma: TurmaCreate, db: Session = Depends(get_db)):
    db_turma = TurmaModel(**turma.dict())
    db.add(db_turma)
    db.commit()
    db.refresh(db_turma)
    return db_turma

@router.get("/turmas/{turma_id}", response_model=Turma)
def read_turma(turma_id: int, db: Session = Depends(get_db)):
    return db.query(TurmaModel).filter(TurmaModel.id == turma_id).first()

@router.get("/turmas/", response_model=list[Turma])
def read_turmas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(TurmaModel).offset(skip).limit(limit).all()

@router.delete("/turmas/{turma_id}")
def delete_turma(turma_id: int, db: Session = Depends(get_db)):
    db_turma = db.query(TurmaModel).filter(TurmaModel.id == turma_id).first()
    if db_turma is None:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    db.delete(db_turma)
    db.commit()
    return {"ok": True} 