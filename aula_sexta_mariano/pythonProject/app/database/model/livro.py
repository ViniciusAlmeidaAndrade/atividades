from sqlalchemy import Column, Integer, String, Boolean

from app.database.db import Base




class Livro(Base):

        """
        Modelo ORM para tabela 'livro'.

        - 'id': Pk autoincrement
        - 'titulo': Titulo(obrigatoria)
        - 'autor': Autor(obigatorio)
        - 'editora': editora(obrigatorio)
        - 'categoria': categoria (enum, obriogatorio)
        - 'ano': Ano de Publicação
        - 'quantidade': Quantidade de Livros (Default=1)
        - 'disponivel': Booleano de disponibilidade (Default=True)
        """
        __tablename__ = "livros"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        titulo = Column(String, index=True, nullable=False)
        autor = Column(String, index=True, nullable=False)
        editora = Column(String, index=True,  nullable=False)
        categoria = Column(Integer, nullable=False)
        ano = Column(Integer, nullable=True)
        qtd_est = Column(Integer, default=1)
        disponivel = Column(Boolean, nullable=False, default=True)

        __table_args__ = (
            CheckConstrain("disponivel in (0,1)", name="ck")
        )
