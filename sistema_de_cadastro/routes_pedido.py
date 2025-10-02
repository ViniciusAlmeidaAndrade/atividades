from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db import get_db
from models import Pedido
from schemas import PedidoCreate, PedidoOut, PedidoUpdate

pedido_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedido_router.post("/adicionar", status_code=status.HTTP_201_CREATED, response_model=PedidoOut)
async def criar_pedido( payload: PedidoCreate, db: AsyncSession = Depends(get_db)):

    novo_pedido = Pedido(
        cliente_id=payload.cliente_id,
        produto=payload.produto,
        valor=payload.valor
    )

    db.add(novo_pedido)
    await db.commit()
    await db.refresh(novo_pedido)

    return novo_pedido


@pedido_router.get("/lista", status_code=status.HTTP_200_OK, response_model=list[PedidoOut])
async def listar_pedidos(db: AsyncSession = Depends(get_db)):

    query = select(Pedido).order_by(Pedido.id.asc())
    resultado = await db.execute(query)
    lista_pedidos = resultado.scalars().all()

    if not lista_pedidos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")

    return lista_pedidos


@pedido_router.patch("/{id}/atualizar", status_code=status.HTTP_200_OK, response_model=PedidoOut)
async def atualizar_pedido(id: int, payload: PedidoUpdate, db: AsyncSession = Depends(get_db)):
    pedido = await db.get(Pedido, id)

    if not pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")

    pedido.cliente_id = payload.cliente_id
    pedido.produto = payload.produto
    pedido.valor = payload.valor

    await db.commit()
    await db.refresh(pedido)

    return pedido


@pedido_router.delete("/{id}/deletar", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_pedido(id: int, db: AsyncSession = Depends(get_db)):

    pedido = await db.get(Pedido, id)

    if not pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")

    await db.delete(pedido)
    await db.commit()

    return None