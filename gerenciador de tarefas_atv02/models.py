import sqlite3

try:
    conn = sqlite3.connect("gerenciador de tarefas_atv02\bilioteca.db")
    cursor = conn.cursor()

    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS livros(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     titulo TEXT NOT NULL,
    #     autor TEXT NOT NULL,
    #     ano INTEGER,
    #     disponivel BOOLEAN NOT NULL
    #     )
    # """)

    # conn.commit()

    class Livros:
        def __init__(self, titulo, autor, ano, disponivel=True):
            self.titulo = titulo
            self.autor = autor
            self.ano = ano
            self.disponivel = disponivel

except conn.DatabaseError as erro:
    print(f"Erro ao conectar com o banco de dados: {erro}")

