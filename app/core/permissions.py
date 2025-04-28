from fastapi import HTTPException

def checar_permissao(usuario, grupo_necessario):
    grupos = [g.nome for g in usuario.grupos]
    if grupo_necessario not in grupos and "admin" not in grupos:
        raise HTTPException(status_code=403, detail="Permissão negada") 