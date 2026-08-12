# Tabela de categoria 
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100), nullable=False, unique=True)
    ativo = Column(Boolean, default=True)

    #Relacionamento
    #lazy="select" - carrega os produtos apenas quando necessario.
    produtos = relationship("Produto", back_populates="categoria", lazy="select")

