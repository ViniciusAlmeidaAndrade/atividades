from models import conn, cursor, Livros


livro = Livros("Desaventura em série-mau começo","Lemony Snicket",2004, True)
#CREATE - Adcionar novo livro

cursor.execute('''
    INSERT INTO livros (titulo, autor, ano, disponivel)
    VALUES(?,?,?,?);'''
    , ( livro.titulo,
        livro.autor,
        livro.ano,
        livro.disponivel))

# cursor.execute('''
#     INSERT INTO livros (titulo, autor, ano, disponivel)
#     VALUES(?,?,?,?);

# ''',("Desaventura em série-mau começo","Lemony Snicket",2004, True))
conn.commit()
conn.close()

#READ - Listar todos os livros
cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()
for livro in livros:
    print(livro)
conn.commit()

#READ - Buscar livros por titulo ou autor
cursor.execute("SELECT * FROM livros")
livros = cursor.fetchone("titulo" or "autor")# Acho que vou ter qu efazer um filter
for livro in livros:
    print(livro)
conn.commit()


#UPDATE - Atualizar status de disponibilidade
cursor.execute("""
    UPDATE livros
    SET disponivel = ?
    where disponivel = ?
""",(""))
conn.commit()

#DELETE - Remover livro
cursor.execute("""
DELETE FROM livros
WHERE
""", (""))

conn.commit()

for cursor in cursor:
    print(cursor)
cursor.close()
conn.close()

