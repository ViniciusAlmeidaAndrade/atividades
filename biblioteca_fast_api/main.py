from fastapi import FastAPI
import uvicorn
from dependencies import criar_tabelas  
from routes_livro import routes_crud

app = FastAPI()

@app.on_event("startup")
def startup_event():
    criar_tabelas()


app.include_router(routes_crud)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)