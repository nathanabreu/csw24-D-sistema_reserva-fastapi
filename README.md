# Sistema de Reservas Acadêmicas - FastAPI

## Como rodar o projeto localmente

1. Crie um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Rode a aplicação:
```
uvicorn app.main:app --reload
```

4. Acesse a documentação:
- Swagger: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc
