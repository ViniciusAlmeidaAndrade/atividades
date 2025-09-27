from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.

DB_URL = "sqlite+aiosqlite:///./biblioteca.db"

engine = create_async_engine(DB_URL, future = True)
AsyncSessionLocal = async_sessionmmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    """
    Fornece uma sessão assincrona do SQLAlchemy por requisição a api.

    :return: 'AsyncSession' com commit/ rollback automatico.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as err:
            print("Erro ao executar comando no banco: {}".format(err))
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro no serviço do banco: ")


