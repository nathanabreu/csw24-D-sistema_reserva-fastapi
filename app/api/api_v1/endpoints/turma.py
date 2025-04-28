from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel

@router.post("/turmas/", response_model=Turma)
def create_turma(turma: TurmaCreate, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == turma.professor_id).first()
    checar_permissao(usuario, "coordenador")
    db_turma = TurmaModel(**turma.dict())
    db.add(db_turma)
    db.commit()
    db.refresh(db_turma)
    return db_turma 