from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tiporecurso import TipoRecurso, TipoRecursoCreate
from app.models.tiporecurso import TipoRecurso as TipoRecursoModel
from app.db.session import get_db
from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel

router = APIRouter(tags=["Tipos de Recurso"])

@router.post("/tipos_recurso/", response_model=TipoRecurso)
def create_tiporecurso(tiporecurso: TipoRecursoCreate, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == tiporecurso.usuario_id).first()
    checar_permissao(usuario, "admin")
    db_tiporecurso = TipoRecursoModel(**tiporecurso.dict())
    db.add(db_tiporecurso)
    db.commit()
    db.refresh(db_tiporecurso)
    return db_tiporecurso

@router.get("/tipos_recurso/{tiporecurso_id}", response_model=TipoRecurso)
def read_tiporecurso(tiporecurso_id: int, db: Session = Depends(get_db)):
    return db.query(TipoRecursoModel).filter(TipoRecursoModel.id == tiporecurso_id).first()

@router.get("/tipos_recurso/", response_model=list[TipoRecurso])
def read_tiposrecurso(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(TipoRecursoModel).offset(skip).limit(limit).all()

@router.delete("/tipos_recurso/{tiporecurso_id}")
def delete_tiporecurso(tiporecurso_id: int, db: Session = Depends(get_db)):
    db_tiporecurso = db.query(TipoRecursoModel).filter(TipoRecursoModel.id == tiporecurso_id).first()
    if db_tiporecurso is None:
        raise HTTPException(status_code=404, detail="Tipo de recurso não encontrado")
    db.delete(db_tiporecurso)
    db.commit()
    return {"ok": True} 