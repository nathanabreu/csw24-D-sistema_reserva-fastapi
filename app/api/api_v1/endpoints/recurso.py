from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.recurso import Recurso, RecursoCreate
from app.models.recurso import Recurso as RecursoModel
from app.db.session import get_db
from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel
from app.api.auth import get_usuario_atual

router = APIRouter(tags=["Recursos"])

@router.post("/recursos/", response_model=Recurso)
def create_recurso(recurso: RecursoCreate, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "admin")
    db_recurso = RecursoModel(**recurso.dict())
    db.add(db_recurso)
    db.commit()
    db.refresh(db_recurso)
    return db_recurso

@router.get("/recursos/{recurso_id}", response_model=Recurso)
def read_recurso(recurso_id: int, db: Session = Depends(get_db)):
    return db.query(RecursoModel).filter(RecursoModel.id == recurso_id).first()

@router.get("/recursos/", response_model=list[Recurso])
def read_recursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(RecursoModel).offset(skip).limit(limit).all()

@router.delete("/recursos/{recurso_id}")
def delete_recurso(recurso_id: int, db: Session = Depends(get_db), current_user = Depends(get_usuario_atual)):
    checar_permissao(current_user, "admin")
    db_recurso = db.query(RecursoModel).filter(RecursoModel.id == recurso_id).first()
    if db_recurso is None:
        raise HTTPException(status_code=404, detail="Recurso não encontrado")
    db.delete(db_recurso)
    db.commit()
    return {"ok": True} 