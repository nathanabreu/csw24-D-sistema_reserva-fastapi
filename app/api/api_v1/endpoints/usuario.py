from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel

@router.post("/usuarios/", response_model=Usuario)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_logado = db.query(UsuarioModel).filter(UsuarioModel.id == usuario.id).first()
    checar_permissao(usuario_logado, "admin")
    db_usuario = UsuarioModel(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario 