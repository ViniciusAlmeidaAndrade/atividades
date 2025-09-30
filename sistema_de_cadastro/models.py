from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, DateTime
from db import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)


class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    produto = Column(String, nullable=False)
    valor = Column(Numeric, nullable=False)
    data = Column(DateTime, nullable=False, default=datetime.now)