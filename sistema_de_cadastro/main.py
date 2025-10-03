from settings import create_app
from routes_cliente import cliente_router
from routes_pedido import pedido_router
from db import engine, Base

app = create_app()

app.include_router(cliente_router)
app.include_router(pedido_router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
