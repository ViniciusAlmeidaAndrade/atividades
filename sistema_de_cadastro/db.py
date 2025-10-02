from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DB_URL = 'sqlite+aiosqlite:///cliente_pedido.sqlite3'

engine = create_async_engine(DB_URL, future=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    """
    Fornece uma sessão assincrona do SQLAlchemy por requisição a api.

    :return: 'AsyncSession' com commit/ rollback automatico.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as err:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro no serviço do banco {err}")
