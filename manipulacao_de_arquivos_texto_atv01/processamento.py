arquivo_entrada = 'manipulacao_de_arquivos_texto_atv01/entrada.txt'
arquivo_saida = 'manipulacao_de_arquivos_texto_atv01/saida.txt'

linhas_processadas = []

try:
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if 'ignorar' not in linha.lower():
                linha_modificada = linha.lower().replace('problema', 'desafio')
                
                linhas_processadas.append(linha_modificada + '\n')

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

if linhas_processadas: 
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_processadas)
    print(f"Conteúdo processado e salvo com sucesso em '{arquivo_saida}'.")
else:
    print("Nenhuma linha foi processada ou o arquivo de entrada estava vazio.")