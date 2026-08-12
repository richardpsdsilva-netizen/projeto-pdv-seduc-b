# Instalar as bibliotecas 

no terminal:
```bash
pip install -r requirements.txt
```

# Inicializar o alembic 
no terminal:
```bash
python -m alembic init migrations
```

# Editar o arquivo alembic init - na linha 89:
sqlalchemy.url = 

# Copie os códigos do arquivo migrations/env.py para garantir o funcionamento.


# Gerar a migration
no terminal:
```bash
python -m alembic revision --autogenerate -m "nome do que foi feito"
```

# Aplicar a migration no banco
```bash
python -m alembic upgrade head
```

# Rodar o código
```bash
python -m uvicorn app.main:app --reload
```
