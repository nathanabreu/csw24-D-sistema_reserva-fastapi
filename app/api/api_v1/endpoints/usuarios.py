from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, Usuario as UsuarioSchema
from app.api.auth import get_usuario_atual

router = APIRouter()

@router.post("/", response_model=UsuarioSchema)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    db_usuario = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Username já registrado")
    
    senha_hash = Usuario.gerar_hash_senha(usuario.senha)
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        username=usuario.username,
        primeiro_nome=usuario.primeiro_nome,
        ultimo_nome=usuario.ultimo_nome,
        tipo=usuario.tipo,
        senha_hash=senha_hash
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/", response_model=List[UsuarioSchema])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_usuario_atual)):
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    return usuarios

@router.get("/{usuario_id}", response_model=UsuarioSchema)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_usuario_atual)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@router.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(db_usuario)
    db.commit()
    return {"ok": True} 