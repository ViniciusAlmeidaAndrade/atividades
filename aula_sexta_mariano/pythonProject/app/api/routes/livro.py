from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.schemas.livro import LivroOutTiago, LivroCreated
from app.database.db import get_db

router = APIRouter(
    prefix="/livro",
    tags=["Livros"]
)

@router.post("/cadastrar", response_model=LivroOutTiago, status_code= status.HTTP_201_CREATED)

async def adicionar_livro(
        payload = LivroCreated, db: AsyncSession = Depends(get_db)
):
    """

    :param payload: Dados do livro conforme schema.
    :param db: Inicia a sessão
    :return: Retorna livro criado
    """

    novo = Livro(
        titulo=payload.titulo.strip()
        autor = payload.autor.strip()
        editora = payload.editora.strip()
        categoria = payload.categoria.strip()
        ano = payload.ano.strip()
        qtd_est = payload.qtd_est.strip()
        disponivel = payload.disponivel.strip()
    )

    # passando chave e valor dinamicamente por atributo
    novo_tiago = Livro(**dict(payload))

    db.add(novo_tiago)
    await db.flush()
    await db.refresh(novo)
    return livro_to_out(novo)