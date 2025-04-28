from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.aula import Aula, AulaCreate
from app.models.aula import Aula as AulaModel
from app.db.session import get_db
from app.core.permissions import checar_permissao
from app.api.auth import get_usuario_atual

router = APIRouter(tags=["Aulas"])

@router.post("/aulas/", response_model=Aula)
def create_aula(aula: AulaCreate, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "professor")
    db_aula = AulaModel(**aula.dict())
    db.add(db_aula)
    db.commit()
    db.refresh(db_aula)
    return db_aula

@router.get("/aulas/{aula_id}", response_model=Aula)
def read_aula(aula_id: int, db: Session = Depends(get_db)):
    return db.query(AulaModel).filter(AulaModel.id == aula_id).first()

@router.get("/aulas/", response_model=list[Aula])
def read_aulas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AulaModel).offset(skip).limit(limit).all()

@router.delete("/aulas/{aula_id}")
def delete_aula(aula_id: int, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "professor")
    db_aula = db.query(AulaModel).filter(AulaModel.id == aula_id).first()
    if db_aula is None:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    db.delete(db_aula)
    db.commit()
    return {"ok": True} 