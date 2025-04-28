from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "chave-super-secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha_plana, hash_senha):
    return pwd_context.verify(senha_plana, hash_senha)

def gerar_hash_senha(senha):
    return pwd_context.hash(senha)

def criar_token_acesso(dados: dict, expires_delta: Optional[timedelta] = None):
    to_encode = dados.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
