from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.predio import Predio as PredioModel
from app.schemas.predio import Predio, PredioCreate
from app.db.session import get_db
from app.core.permissions import checar_permissao
from app.api.auth import get_usuario_atual

router = APIRouter(tags=["Prédios"])

@router.post("/predios/", response_model=Predio)
def create_predio(predio: PredioCreate, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "admin")
    db_predio = PredioModel(**predio.dict())
    db.add(db_predio)
    db.commit()
    db.refresh(db_predio)
    return db_predio

@router.get("/predios/{predio_id}", response_model=Predio)
def read_predio(predio_id: int, db: Session = Depends(get_db)):
    return db.query(PredioModel).filter(PredioModel.id == predio_id).first()

@router.get("/predios/", response_model=list[Predio])
def read_predios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(PredioModel).offset(skip).limit(limit).all()

@router.delete("/predios/{predio_id}")
def delete_predio(predio_id: int, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "admin")
    db_predio = db.query(PredioModel).filter(PredioModel.id == predio_id).first()
    if db_predio is None:
        raise HTTPException(status_code=404, detail="Prédio não encontrado")
    db.delete(db_predio)
    db.commit()
    return {"ok": True} 