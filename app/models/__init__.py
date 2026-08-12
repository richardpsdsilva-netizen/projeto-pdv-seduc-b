from app.models import categoria
from app.models import produto
from app.models import usuarios
from app.models import movimentacao

# Gerar a migration

# python -m alembic revision --autogenerate -m "Criar tabela categorias e produtos."

# aplicar a migration
# python -m alembic upgrade head