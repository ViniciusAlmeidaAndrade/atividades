from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db import get_db
from models import Cliente, Pedido
from site import Cliente


cliente_router = APIRouter(prefix="/clientes", tags=["clientes"])
cliente_router = APIRouter(prefix="/routes", tags=["clientes"])