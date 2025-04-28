from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import init_db
from app.api.auth import router as auth_router

# Importações dos modelos para garantir que todas as tabelas sejam registradas
from app.models import (
    usuario,
    grupo,
    usuarios_grupos,
    turma,
    horario,
    turmas_alunos,
    reserva,
    predio,
    sala,
    requisito,
    disciplina_curriculo,
    curriculo,
    disciplina,
    aula,
    tiporecurso,
    recurso,
    pedido
)

app = FastAPI(
    title="Sistema de Reservas Acadêmicas",
    description="API Backend para gerenciamento de disciplinas, turmas, salas e reservas de recursos.",
    version="1.0.0"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialização do banco
@app.on_event("startup")
async def startup():
    init_db()

# Rota raiz
@app.get("/")
def read_root():
    return {"mensagem": "API de Backend operando com sucesso!"}

# Inclusão de rotas após a criação do app
app.include_router(auth_router)

from app.api.api_v1.endpoints.usuarios import router as usuarios_router
app.include_router(usuarios_router)

from app.api.api_v1.endpoints.disciplinas import router as disciplinas_router
app.include_router(disciplinas_router)

from app.api.api_v1.endpoints.turmas import router as turmas_router
app.include_router(turmas_router)

from app.api.api_v1.endpoints.salas import router as salas_router
app.include_router(salas_router)

from app.api.api_v1.endpoints.reservas import router as reservas_router
app.include_router(reservas_router)

from app.api.api_v1.endpoints.pedido import router as pedido_router
app.include_router(pedido_router)

from app.api.api_v1.endpoints.recurso import router as recurso_router
app.include_router(recurso_router)

from app.api.api_v1.endpoints.tiporecurso import router as tiporecurso_router
app.include_router(tiporecurso_router)

from app.api.api_v1.endpoints.aula import router as aula_router
app.include_router(aula_router)