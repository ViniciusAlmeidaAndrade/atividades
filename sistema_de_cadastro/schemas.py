from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import Optional


class ClienteBase(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do cliente")
    email: EmailStr = Field(..., description="Email do cliente")
    telefone: str = Field(..., min_length=3, max_length=20, description="Telefone do cliente")

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, description="Nome do cliente")
    email: Optional[EmailStr] = Field(None, description="Email do cliente")
    telefone: Optional[str] = Field(None, min_length=3, max_length=20, description="Telefone do cliente")


class ClienteOut(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PedidoBase(BaseModel):
    cliente_id: int = Field(..., description="ID do cliente associado ao pedido.")
    produto: str = Field(..., min_length=3, max_length=50, description="Nome do produto.")
    valor: float = Field(..., ge=0, description="O valor total do pedido deve ser igual ou maior que 0.")

class PedidoCreate(PedidoBase):
    pass

class PedidoUpdate(BaseModel):
    cliente_id: Optional[int] = Field(None, description="ID do cliente associado ao pedido.")
    produto: Optional[str] = Field(None, min_length=3, max_length=50, description="Nome do produto.")
    valor: Optional[float] = Field(None, gt=0, description="O valor total do pedido. Deve ser positivo.")

class PedidoOut(PedidoBase):
    id: int
    data: datetime
    model_config = ConfigDict(from_attributes=True)