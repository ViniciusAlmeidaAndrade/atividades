from typing import Optional

from pydantic import BaseModel, Field


class LivroCreated(BaseModel):
    titulo: str = Field(..., min_length=10)
    autor: str = Field(..., min_length=10)
    editora: str = Field(..., min_length=5)
    categoria: int
    ano: Optional[int] = Field(None, le=9999)
    qtd_est: int = Field(default=1)
    disponivel: bool = True

class LivroOut(BaseModel):
    id = int
    titulo: str
    autor: str
    editora: str
    categoria: int
    ano: Optional[int]
    qtd_est: int
    disponivel: bool

class LivroOutTiago(LivroCreated):
    id = int