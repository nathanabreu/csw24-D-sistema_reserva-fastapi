from app.db.session import Base

# Aqui futuramente registramos os modelos, exemplo:
# from .usuario import Usuario
# from .disciplina import Disciplina
from app.models.usuario import *
from app.models.disciplina import *
from app.models.turma import *
from app.models.sala import *
from app.models.reserva import *
