from database import init_db
from livro import adicionar_livro, listar_livros, buscar_livros, atu_disp, deletar_fisico,excluir_livro, Categoria, Status


def menu_biblioteca():
    init_db()
    while True:
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro por título, autor ou editora")
        print("4 - Atualizar Status")
        print("5 - Remover livro permanentemente")
        print("6 - Excluir livro")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            livro_titulo = input("Digite o título do livro: ").strip().lower()
            livro_autor = input("Digite o autor do livro: ").strip().lower()
            livro_editora = input("Digite a editora do livro: ").strip().lower()
            
            while True:    
                try:
                    livro_categoria_str = input("Digite a categoria do livro [romance], [acao], [ficcao], [comedia], [suspense], [terror], [outros]: ").strip().lower()
                    livro_categoria = Categoria[livro_categoria_str]
                    break
                except KeyError:
                    print("Categoria inválida! Tente novamente.")

            while True:
                try:
                    livro_ano = int(input("Digite o ano de publicação do livro: "))
                    break
                except ValueError:
                    print("Ano inválido! Digite um número.")

            while True:
                try:
                    livro_disponivel = int(input("O livro está disponível? (Digite 1 para sim e 0 para não): "))
                except ValueError:
                    print("Valor inválido! Digite 1 para sim e 0 para não.")
                
                if livro_disponivel in (0, 1):
                    break
                else:
                    print("Valor inválido! Digite 1 para sim e 0 para não.")

            while True:
                try:
                    livro_status_str = input("Digite o status do livro [ativo], [inativo], [excluido]: ").strip().lower()
                    livro_status = Status[livro_status_str]
                    break
                except KeyError:
                    print("Status inválido! Tente novamente.")
                    
            adicionar_livro(livro_titulo, livro_autor, livro_editora, livro_categoria, livro_ano, livro_disponivel, livro_status)
        
        elif opcao == "2":

            livros = listar_livros()
            if not livros:
                print("Nenhum livro cadastrado na biblioteca.")
            else:
                for livro in livros:
                    livro_dict = dict(livro)
                    livro_dict["disponivel"] = "Sim" if livro_dict["disponivel"] == 1 else "Não"
                    print(livro_dict)
                    

        elif opcao == "3":
            procurar = input("Digite o titulo, autor ou editora do livro que deseja procurar: ").strip().lower()
            
            resultado = buscar_livros(procurar)
            if not resultado:
                print("Nenhum livro encontrado com essas características.")
            else:
                for livro in resultado:
                    livro_dict = dict(livro)
                    livro_dict["disponivel"] = "Sim" if livro_dict["disponivel"] == 1 else "Não"
                    print(livro_dict)

        
        elif opcao == "4":
            while True:
                try:
                    LivroID = int(input("Digite o id do livro que deseja atualizar a disponibilidade: "))
                    livro_disponivel = int(input("O livro está disponível? (Digite 1 para sim e 0 para não): "))
                    if livro_disponivel in (0, 1):
                        break
                    else:
                        print("Valor inválido! Digite 1 para sim e 0 para não.")
                except ValueError:
                    print("Valor inválido! O ID deve ser número.")
                
            
            if atu_disp(LivroID, livro_disponivel):
                print("Disponibilidade atualizada com sucesso!")
            else:
                print("Livro não encontrado ou erro ao atualizar.")
        
        elif opcao == "5":
            while True:
                try:
                    LivroID = int(input("Digite o id do livro que deseja deletar permanentemente: "))
                    break
                except ValueError:
                    print("Valor inválido! O ID deve ser número.")


            if deletar_fisico(LivroID):
                print("Livro removido com sucesso!")
            else:
                print("Livro não encontrado ou erro ao remover.")

        elif opcao == "6":
            while True:
                try:
                    LivroID = int(input("Digite o id do livro que deseja excluir: "))
                    break
                except ValueError:
                    print("Valor inválido! O ID deve ser número.")

            if excluir_livro(LivroID):
                print("Livro excluído com sucesso!")
            else:
                print("Livro não encontrado ou erro ao excluir.")
        
        elif opcao == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    menu_biblioteca()

