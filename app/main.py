from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import init_db

app = FastAPI(
    title="Sistema de Reservas Acadêmicas",
    description="API Backend para gerenciamento de disciplinas, turmas, salas e reservas de recursos.",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialização do banco de dados
@app.on_event("startup")
async def startup():
    init_db()

# Rota de exemplo
@app.get("/")
def read_root():
    return {"mensagem": "API de Backend operando com sucesso!"}

from app.api.usuarios import router as usuarios_router
app.include_router(usuarios_router)

from app.api.disciplinas import router as disciplinas_router
app.include_router(disciplinas_router)

from app.api.turmas import router as turmas_router
app.include_router(turmas_router)

from app.api.salas import router as salas_router
app.include_router(salas_router)

from app.api.reservas import router as reservas_router
app.include_router(reservas_router)
