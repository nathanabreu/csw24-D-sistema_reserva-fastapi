from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.auth import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        tipo = payload.get("tipo")
        if tipo is None:
            raise HTTPException(status_code=403, detail="Tipo de usuário não encontrado")
        return {"tipo": tipo, "email": payload.get("sub")}

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

def require_roles(*allowed_roles):
    def role_checker(current_user=Depends(get_current_user)):
        if current_user["tipo"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Acesso negado para este perfil de usuário.")
    return role_checker
