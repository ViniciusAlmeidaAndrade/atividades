from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, session
from starlette import status
from db import get_db
from models import Cliente

cliente_router = APIRouter(prefix="/clientes", tags=["clientes"])

@cliente_router.post("/cadastrar", status_code=status.HTTP_201_CREATED)#, response_model=)
async def cadastrar_cliente( payload : Cliente, db: AsyncSession = Depends(get_db)):
    novo_cliente = Cliente(
        nome=payload.nome.strip(),
        email=payload.email.strip(),
        telefone=payload.telefone.strip()

    )

    db.add(novo_cliente)
    await db.commit()
    await db.refresh(novo_cliente)
    return {"mensage":f"Cliente {novo_cliente.nome} de id:[{novo_cliente.id}] cadastrado com sucesso!"}

@cliente_router.get("/", status_code=status.HTTP_200_OK)
async def listar_clientes(db: AsyncSession = Depends(get_db)):
    query= select(Cliente).order_by(Cliente.nome.asc())

    resultado = await db.execute(query)

    lista_clientes = resultado.scalars().all()
    if not lista_clientes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Nenhum cliente cadastrado")
    return lista_clientes

@cliente_router.patch("/{id}", status_code=status.HTTP_200_OK)
async def atualizar_cliente(id: int, db: AsyncSession = Depends(get_db)):
    

@cliente_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(id: int, db: AsyncSession = Depends(get_db)):
    del_cliente = db.query(Cliente).filter(Cliente.id == id).scalar()
    if not del_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cliente não encontrado")
    await db.delete(del_cliente)
    await db.commit()

    return None