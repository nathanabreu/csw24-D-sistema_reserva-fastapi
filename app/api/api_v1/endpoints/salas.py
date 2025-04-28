from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.sala import Sala as SalaModel
from app.schemas.sala import Sala, SalaCreate
from app.db.session import get_db

router = APIRouter()

@router.post("/salas/", response_model=Sala)
def create_sala(sala: SalaCreate, db: Session = Depends(get_db)):
    db_sala = SalaModel(**sala.dict())
    db.add(db_sala)
    db.commit()
    db.refresh(db_sala)
    return db_sala

@router.get("/salas/{sala_id}", response_model=Sala)
def read_sala(sala_id: int, db: Session = Depends(get_db)):
    return db.query(SalaModel).filter(SalaModel.id == sala_id).first()

@router.get("/salas/", response_model=list[Sala])
def read_salas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(SalaModel).offset(skip).limit(limit).all()

@router.delete("/salas/{sala_id}")
def delete_sala(sala_id: int, db: Session = Depends(get_db)):
    db_sala = db.query(SalaModel).filter(SalaModel.id == sala_id).first()
    if db_sala is None:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    db.delete(db_sala)
    db.commit()
    return {"ok": True} 