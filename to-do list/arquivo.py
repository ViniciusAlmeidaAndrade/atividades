from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
class Tarefa (Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    prioridade = Column(String, nullable=False)
    concluida = Column(Boolean, nullable=False, default=False)
    categoria = Column(String, nullable=True)
    data_criacao = Column(DateTime, nullable=False, default=datetime.now)

engine = create_engine('sqlite:///Banco.db')
Session = sessionmaker(bind=engine)
sessao = Session()

def criar_tabela():
    Base.metadata.create_all(engine)


def adicionar_tarefa(sessao, titulo, descricao, prioridade, categoria):

    try:
        if not titulo or titulo.strip() == '':
            print('Cadastre uma tarefa com título')
            return

        prioridades_validas = ['alta','media','baixa']
        if prioridade not in prioridades_validas:
            print(f'Erro: {prioridade} não é valida. Use: "alta","media" ou "baixa" ')
            return

        categorias_validas = ['trabalho','estudo','trabalhos academicos']
        if categoria not in categorias_validas:
            print(f'Erro: {categoria} não é valida. Use: "trabalho","estudo","trabalhos academicos" ')
            return
        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade.lower(),
            categoria=categoria
        )
        sessao.add(nova_tarefa)
        sessao.commit()
        print('Tarefa adicionada com sucesso.')
    except Exception as exc:
        sessao.rollback()
        print(f'Erro ao adicionar tarefa{exc}')


def listar_tarefas(sessao, filtro_prioridade=None, filtro_concluida=None, filtro_categoria=None):

    try:
        pega_tarefas = sessao.query(Tarefa)

        if filtro_prioridade:
            pega_tarefas = pega_tarefas.filter(Tarefa.prioridade == filtro_prioridade)
        if filtro_concluida is not None:
            pega_tarefas = pega_tarefas.filter(Tarefa.concluida == filtro_concluida)
        if filtro_categoria:
            pega_tarefas = pega_tarefas.filter(Tarefa.categoria == filtro_categoria)
        tarefas = pega_tarefas.all()
        return tarefas
    except Exception as exc:
        print(f'Erro ao listar tarefas{exc}')


def marcar_conclusao(sessao, id_tarefa, status_concluido):
    try:
        tarefa = sessao.query(Tarefa).get(id_tarefa)
        if tarefa:
            tarefa.concluida = status_concluido
            sessao.commit()
            if status_concluido:
                concluido_mensagem = 'Concluido'
            else:
                concluido_mensagem = 'Pendente'
            print(f'A Tarefa {tarefa.titulo} de ID:{id_tarefa} foi atualizada como {concluido_mensagem}')
        else:
            print('Tarefa não encontrada')
    except Exception as exc:
        sessao.rollback()
        print(f'Erro ao atualizar a tarefa{exc}')

def excluir_tarefa(sessao, id_tarefa):
    try:
        tarefa = sessao.query(Tarefa).get(id_tarefa)
        if tarefa:
            sessao.delete(tarefa)
            sessao.commit()
            print(f'A Tarefa {tarefa.titulo} de ID:{id_tarefa} foi excluida com sucesso!')
        else:
            print ('Essa tarefa não existe')
    except Exception as exc:
        sessao.rollback()
        print(f'Erro ao excluir tarefa{exc}')

def menu(sessao):

    while True:
        print('\n==============================MENU==================================')
        opcao = input ('''
Digite o numero correpondente para escolher uma das opções abaixo:
[1] Adicionar Tarefa 
[2] Listar Tarefas
[3] Marcar Tarefa como Concluída
[4] Excluir Tarefa
[0] Sair
>>>>>> ''')
        if opcao == '1':
            titulo = input('Titulo: ').strip()
            descricao = input('Descricao: ').strip()
            prioridade = input('Prioridade (alta, media, baixa): ').strip().lower()
            categoria = input('Qual categoria deseja adicionar? (trabalho, estudo, trabalhos academicos): ').strip().lower()
            adicionar_tarefa(sessao, titulo, descricao, prioridade, categoria)
        elif opcao == '2':
            tarefas = sessao.query(Tarefa)
            while True:
                filtrar = input('Gostaria de filtrar as tarefas? (s/n): ').strip().lower()

                if filtrar == 'n':
                    tarefas = listar_tarefas(sessao)
                    break
                elif filtrar == 's':
                    while True:
                        escolha = input('Listar as tarefas concluídas (1), por prioridade (2) ou por categoria (3)? ').strip()

                        if escolha == '1':
                            while True:
                                filtro_concluida_input = input('Mostrar tarefas concluídas (1) ou pendentes (2)? ').strip().lower()
                                if filtro_concluida_input == '1':
                                    tarefas = listar_tarefas(sessao, filtro_concluida=True)
                                    break
                                elif filtro_concluida_input == '2':
                                    tarefas = listar_tarefas(sessao, filtro_concluida=False)
                                    break
                                else:
                                    print('Opção inválida. Digite apenas "1" ou "2".')
                            break
                        elif escolha == '2':
                            while True:
                                prioridade = input('Qual prioridade deseja filtrar? (alta, media, baixa): ').strip().lower()
                                prioridades_validas = ['alta', 'media', 'baixa']
                                if prioridade in prioridades_validas:
                                    tarefas = listar_tarefas(sessao, filtro_prioridade=prioridade)
                                    break
                                else:
                                    print(f"Prioridade inválida. Use: 'alta', 'media' ou 'baixa'.")
                            break
                        elif escolha == '3':
                            while True:
                                categoria_input = input('Qual categoria deseja filtrar? (trabalho [1], estudo [2], trabalho academico [3]): ').strip()
                                if categoria_input == '1':
                                    categoria = 'trabalho'
                                    tarefas = listar_tarefas(sessao, filtro_categoria=categoria)
                                    break
                                elif categoria_input == '2':
                                    categoria = 'estudo'
                                    tarefas = listar_tarefas(sessao, filtro_categoria=categoria)
                                    break
                                elif categoria_input == '3':
                                    categoria = 'trabalhos academicos'
                                    tarefas = listar_tarefas(sessao, filtro_categoria=categoria)
                                    break
                                else:
                                    print("Opção inválida. Por favor, digite 1, 2 ou 3.")
                            break
                        else:
                            print("Entrada inválida. Digite apenas '1' '2' ou  '3'.")
                    break
                else:
                    print("Entrada inválida. Digite apenas 's' ou 'n'.")
            print('\n=========================TAREFAS=============================')
            if tarefas:
                for tarefa in tarefas:
                    if tarefa.concluida:
                        status = 'Concluido'
                    else:
                        status = 'Pendente'
                    data_formatada = tarefa.data_criacao.strftime("%d/%m/%Y %H:%M")

                    print(f'''
                    Tarefa: ID:[{tarefa.id}] 
                    Titulo: {tarefa.titulo} 
                    Descrição: {tarefa.descricao}  
                    prioridade: {tarefa.prioridade} 
                    Status: {status}
                    Categoria: {tarefa.categoria}
                    Data de Criação: {data_formatada}''')
            else:
                print('Nenhum tarefa encontrada.')

        elif opcao == '3':
            while True:
                id_tarefa = input('Digite o ID Tarefa que deseja: ').strip()
                concluido = input('Marcar esse projeto como concluido?(s/n): ').strip().lower()

                if id_tarefa.isdigit():
                    if concluido == 's':
                        marcar_conclusao(sessao, int(id_tarefa), True)
                        break
                    elif concluido == 'n':
                        marcar_conclusao(sessao, int(id_tarefa), False)
                        break
                    else:
                        print("Digite apenas 's' ou 'n'.")
                else:
                    print('ID inválido. Digite apenas números inteiros.')

        elif opcao == '4':
            while True:
                id_tarefa = input("Digite o ID da tarefa para excluir: ")
                if id_tarefa.isdigit():
                    excluir_tarefa(sessao, int(id_tarefa))
                    break
                else:
                    print('ID inválido. Digite apenas números inteiros.')

        elif opcao == '0':
            sessao.close()
            print('Saindo do programa...')
            break

        else:
            print('\nO que foi digitado não é valido. Tente novamente.')

if __name__ == '__main__':
    criar_tabela()
    menu(sessao)