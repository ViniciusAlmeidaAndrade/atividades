from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title="Gestão de Clientes e Pedidos",
        version="1.0.0",
        description="API para gerenciamento de clientes e pedidos usando SQLite + SQLAlchemy(assiíncrono)",
    )

    return app