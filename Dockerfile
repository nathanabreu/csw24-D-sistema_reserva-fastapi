FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expondo porta da aplicação
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
