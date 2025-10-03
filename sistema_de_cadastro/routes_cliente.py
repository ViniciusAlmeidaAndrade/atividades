from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db import get_db
from models import Cliente, Pedido
from schemas import ClienteCreate, ClienteOut, PedidoOut, ClienteUpdate

cliente_router = APIRouter(prefix="/clientes", tags=["clientes"])

@cliente_router.post("/cadastrar", status_code=status.HTTP_201_CREATED, response_model=ClienteOut)
async def cadastrar_cliente( payload : ClienteCreate, db: AsyncSession = Depends(get_db)):

    novo_cliente = Cliente(
        nome=payload.nome,
        email=payload.email,
        telefone=payload.telefone
    )

    db.add(novo_cliente)
    await db.commit()
    await db.refresh(novo_cliente)

    return novo_cliente


@cliente_router.get("/", status_code=status.HTTP_200_OK, response_model=list[ClienteOut])
async def listar_clientes(db: AsyncSession = Depends(get_db)):

    query = select(Cliente).order_by(Cliente.nome.asc())
    resultado = await db.execute(query)
    lista_clientes = resultado.scalars().all()

    if not lista_clientes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhum cliente cadastrado")

    return lista_clientes


@cliente_router.get("/{id}/pedidos", status_code=status.HTTP_200_OK, response_model=list[PedidoOut])
async def pedido_do_cliente(id: int, db: AsyncSession = Depends(get_db)):

    query = (select(Pedido).where(Pedido.cliente_id == id))
    resultado = await db.execute(query)
    pedido_cliente = resultado.scalars().all()

    if not pedido_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum pedido foi encontrado para o cliente de ID: {id}.")

    return pedido_cliente


@cliente_router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=ClienteOut)
async def atualizar_cliente(id: int, payload: ClienteUpdate, db: AsyncSession = Depends(get_db)):
    cliente = await db.get(Cliente, id)

    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="cliente não foi encontrado.")

    if payload.nome is not None:
        cliente.nome = payload.nome
    if payload.email is not None:
        cliente.email = payload.email
    if payload.telefone is not None:
        cliente.telefone = payload.telefone

    await db.commit()
    await db.refresh(cliente)

    return cliente


@cliente_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(id: int, db: AsyncSession = Depends(get_db)):

    cliente = await db.get(Cliente, id)

    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cliente não encontrado")
    await db.delete(cliente)
    await db.commit()

    return None