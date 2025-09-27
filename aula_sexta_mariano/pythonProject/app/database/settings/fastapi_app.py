from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title = "Biblioteca",
        version = "1.0.0",
        description = "API para gestão basica de livros de livros usando SQLite + SQLAlchemy(assincrono)"
    )
    return app