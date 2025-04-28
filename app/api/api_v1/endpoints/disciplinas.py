from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.disciplina import Disciplina as DisciplinaModel
from app.schemas.disciplina import Disciplina, DisciplinaCreate
from app.db.session import get_db

router = APIRouter()

@router.post("/disciplinas/", response_model=Disciplina)
def create_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    db_disciplina = DisciplinaModel(**disciplina.dict())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

@router.get("/disciplinas/{disciplina_id}", response_model=Disciplina)
def read_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    return db.query(DisciplinaModel).filter(DisciplinaModel.id == disciplina_id).first()

@router.get("/disciplinas/", response_model=list[Disciplina])
def read_disciplinas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(DisciplinaModel).offset(skip).limit(limit).all()

@router.delete("/disciplinas/{disciplina_id}")
def delete_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    db_disciplina = db.query(DisciplinaModel).filter(DisciplinaModel.id == disciplina_id).first()
    if db_disciplina is None:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    db.delete(db_disciplina)
    db.commit()
    return {"ok": True} 