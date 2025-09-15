from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker ,declarative_base

engine = create_engine("sqlite:///biblioteca.db")
Base = declarative_base()

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    categoria = Column(Integer, nullable=False)
    ano = Column(Integer)
    disponivel = Column(Integer, default=1)
    livro_status = Column(Integer, default=1)

    __table_args__ = (
        CheckConstraint("disponivel IN (0, 1)", name="disponivel_check"),
    )

    def __repr__(self):
        return f"<Livro(titulo='{self.titulo}', autor='{self.autor}')>"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
