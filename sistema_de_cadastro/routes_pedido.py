from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db import get_db
from models import Pedido

cliente_router = APIRouter(prefix="/routes", tags=["clientes"])

@cliente_router.post("/Adicionar", status_code=status.HTTP_201_CREATED)#, response_model=)
async def novo_pedido( payload = Pedido, db: AsyncSession = Depends(get_db)):
    novo = Pedido(
        cliente_id=payload.cliente_id.strip(),
        produto=payload.produto.strip(),
        valor=payload.valor.strip(),
        data=payload.data.strip()
    )
