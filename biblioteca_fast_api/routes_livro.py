from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from dependencies import pegar_sessao
from database import  Livro 


routes_crud = APIRouter(prefix="/Livros", tags=["Biblioteca"])


@routes_crud.post("/adicionar")
async def adicionar_livro(titulo: str, autor: str, editora: str, categoria: int, ano: int = None, disponivel: int = 1, livro_status: int = 1, session: Session = Depends(pegar_sessao)):

    novo_livro = Livro(titulo=titulo, autor=autor, editora=editora, categoria=categoria, ano=ano, disponivel=disponivel, livro_status=livro_status)
    
    session.add(novo_livro)
    session.commit()

    return {"message": f"Livro {novo_livro.titulo} adicionado com sucesso", "id": novo_livro.id}


@routes_crud.get("/listar")
async def listar_livros(session: Session = Depends(pegar_sessao)):
    livros = session.query(Livro).all()
    if not livros:
        raise HTTPException(status_code=400, detail="Nenhum projeto encontrado ")
    
    return livros

@routes_crud.get("/buscar/{id}")
async def buscar_livro(id: int, session: Session = Depends(pegar_sessao)):
    livro = session.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    return livro

@routes_crud.patch("/atualizar/{id}")
async def atualizar_livro(id: int, titulo: str = None, autor: str = None, editora: str = None, categoria: int = None, ano: int = None, disponivel: int = None, livro_status: int = None, session: Session = Depends(pegar_sessao)):
    livro = session.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    if titulo is not None:
        livro.titulo = titulo
    if autor is not None:
        livro.autor = autor
    if editora is not None:
        livro.editora = editora
    if categoria is not None:
        livro.categoria = categoria
    if ano is not None:
        livro.ano = ano
    if disponivel is not None:
        livro.disponivel = disponivel
    if livro_status is not None:
        livro.livro_status = livro_status
    
    session.commit()
    return {"message": f"Livro {livro.titulo} atualizado com sucesso"}  

@routes_crud.delete("/deletar_fisico/{id}")
async def deletar_livro(id: int, session: Session = Depends(pegar_sessao)):       
    livro = session.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    session.delete(livro)
    session.commit()
    return {"message": f"Livro {livro.titulo} deletado com sucesso"}

@routes_crud.put("/excluir/{id}")
async def excluir_livro(id: int, session: Session = Depends(pegar_sessao)):
    livro = session.query(Livro).filter(Livro.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    livro.livro_status = 9  
    
    session.commit()
    return {"message": f"Livro {livro.titulo} marcado como excluído com sucesso"}

