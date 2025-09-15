from database import Base, SessionLocal, engine

def pegar_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def criar_tabelas():
    Base.metadata.create_all(bind=engine)
