from app.core.permissions import checar_permissao
from app.models.usuario import Usuario as UsuarioModel

@router.post("/disciplinas/", response_model=Disciplina)
def create_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == disciplina.usuario_id).first()
    checar_permissao(usuario, "coordenador")
    db_disciplina = DisciplinaModel(**disciplina.dict())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina 