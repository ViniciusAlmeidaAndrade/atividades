arquivo = open("treinando_man_arq/dados.txt", "r")

#devolve todo o condeudo do arquivo
conteudo_r = arquivo.read()
#devolve uma linha do arquivo por vez
conteudo_rl = arquivo.readline()
#devolve uma lista com todas as linhas do arquivo
conteudo_rls = arquivo.readlines()


print("Nome do Arquivo", arquivo.name)
print("modo do Arquivo", arquivo.mode)
print("Arquivo fechado", arquivo.closed)

print(type(conteudo_r))
# representação informal mostra apenas o conteudo 
# sem querbra de linha e aspas 
print(conteudo_r)
#'representação oficial do conteudo como o dev escreveu
print(repr(conteudo_r))
print(repr(conteudo_rl))
print(repr(conteudo_rls))
#Após utilizar qualquer um dos métodos para leitura do arquivo apresentado, não podemos utilizá-los novamente. Isso acontece porque o cursor estará posicionado ao final do arquivo, e as chamadas aos métodos read, readline ou readlines retornarão vazias.

# !Se quiser exibir o conteúdo novamente, é necessário fechar e reabrir o arquivo ou utilizando o método seek(0) 

arquivo.close()
print("Arquivo fechado", arquivo.closed)     


# Abre o arquivo (o ponteiro está na posição 0)
arquivo = open("treinando_man_arq/dados.txt", "r")

# Lê o arquivo por completo
conteudo_completo = arquivo.read()
print("Conteúdo completo:")
print(repr(conteudo_completo))

# Move o ponteiro de volta para a posição 0
arquivo.seek(0) 

# Lê a primeira linha (o ponteiro avança)
primeira_linha = arquivo.readline()
print("\nPrimeira linha:")
print(repr(primeira_linha))

# Move o ponteiro de volta para a posição 0
arquivo.seek(0)

# Lê todas as linhas em uma lista (o ponteiro avança para o final)
todas_linhas = arquivo.readlines()
print("\nTodas as linhas em uma lista:")
print(repr(todas_linhas))

# Lembre-se de fechar o arquivo no final
arquivo.close()

#_______________________________write, 'w'_______________________________
#pode ser feito dos dois jeitos a baixo e vai criar um arquivo com essas coisas
arquivo_escrita = open("treinando_man_arq/dados_escrita.txt", "w")
arquivo_escrita.write("é isso ai")
arquivo_escrita.write("\nsegundo é isso ai")
arquivo_escrita.close()


linhas = ["é isso ai,",
    "\nsegundo é isso ai"]

arquivo_escrita = open("dados_escrita.txt", "w")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

print("interando o arquivo escrito")

with open("dados_escrita.txt", "r") as arquivo:
    for linha in arquivo:
        print(repr(linha))
    print("fim do Arquivo", arquivo.name)