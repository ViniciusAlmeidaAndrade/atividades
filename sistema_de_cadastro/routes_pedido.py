from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import defer
from starlette import status
from db import get_db
from models import Pedido

pedido_router = APIRouter(prefix="/routes", tags=["clientes"])

@pedido_router.post("/Adicionar", status_code=status.HTTP_201_CREATED)#, response_model=)
async def criar_pedido( payload = Pedido, db: AsyncSession = Depends(get_db)):

    novo_pedido = Pedido(
        cliente_id=payload.cliente_id.strip(),
        produto=payload.produto.strip(),
        valor=payload.valor.strip(),
        data=payload.data.strip()
    )

    db.add(novo_pedido)
    await db.commit()
    await db.refresh(novo_pedido)
    return {"mensage": f"Pedido feito com sucesso!"}

@pedido_router.get("/", status_code=status.HTTP_200_OK)
async def listar_pedidos(db: AsyncSession = Depends(get_db)):

    query = select(Pedido).order_by(Pedido.id.asc())
    resultado = await db.execute(query)
    lista_pedidos = await resultado.scalar()

    if not lista_pedidos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")

    return lista_pedidos

@pedido_router.patch("/{id}", status_code=status.HTTP_200_OK)
async def atualizar_pedido(id: int, db: AsyncSession = Depends(get_db)):
    query = (select(Pedido).where(Pedido.id == id))
    resultado = await db.execute(query)
    atu_pedido = resultado.scalar_one_or_none()

    if not atu_pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")

    pedido.cliente_id = payload.cliente_id
    pedido.produto = payload.produto
    pedido.valor = payload.valor

    await db.commit()
    await db.refresh(atu_pedido)

    return atu_pedido

@pedido_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_pedido(id: int, db: AsyncSession = Depends(get_db)):

    query = (select(Pedido).where(Pedido.id == id))
    resultado = await db.execute(query)
    del_pedido = resultado.scalar_one_or_none()

    if not del_pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido foi encontrado.")
    await db.commit()

    return None