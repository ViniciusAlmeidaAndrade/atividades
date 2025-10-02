from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class ClienteBase(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do cliente")
    email: EmailStr = Field(..., min_length=3, description="Email do cliente")
    telefone: str = Field(..., min_length=3, max_length=20, description="Telefone do cliente")

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PedidoBase(BaseModel):
    cliente_id: int = Field(..., description="ID do cliente associado ao pedido.")
    produto: str = Field(..., min_length=3, max_length=50, description="Nome do produto.")
    valor: float = Field(..., gt=0, description="O valor total do pedido. Deve ser um valor positivo.")

class PedidoCreate(PedidoBase):
    pass

class PedidoOut(PedidoBase):
    id: int
    data: datetime
    model_config = ConfigDict(from_attributes=True)