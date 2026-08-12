from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

#Tabela
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    #perfil do usuário: "admin" ou "operador"
    role = Column(String(20), nullable=False, default="operador")

    # Permite desativar um usuario sem excluir ele do db
    ativo = Column(Boolean, default=True)
    criando_em = Column(DateTime, server_default=func.now())
   