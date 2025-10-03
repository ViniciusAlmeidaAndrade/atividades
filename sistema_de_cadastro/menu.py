import requests
import sys

API_URL = "http://127.0.0.1:8000"


def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")
    while True:
        nome = input('Nome: ').strip()
        if nome:
            break
        print("Nome não pode ser vazio. Tente novamente.")

    while True:
        email = input('Email: ').strip()
        if email:
            break
        print("Email não pode ser vazio. Tente novamente.")

    while True:
        telefone = input('Telefone: ').strip()
        if telefone:
            break
        print("Telefone não pode ser vazio. Tente novamente.")

    resp = requests.post(f"{API_URL}/clientes/cadastrar", json={
        "nome": nome,
        "email": email,
        "telefone": telefone
    })

    print("\nResposta do Servidor:", resp.json())


def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    resp = requests.get(f"{API_URL}/clientes/")
    resp.raise_for_status()

    clientes = resp.json()
    if clientes:
        print("\nClientes encontrados:")
        for cliente in clientes:
            print(
                f"ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']} | Telefone: {cliente['telefone']}")
    else:
        print("\nNenhum cliente cadastrado.")


def listar_pedidos_de_cliente():
    print("\n--- PEDIDOS DE UM CLIENTE ---")
    while True:
        cliente_id_input = input('ID do Cliente: ').strip()
        if cliente_id_input.isdigit():
            cliente_id = int(cliente_id_input)
            break
        print('ID inválido. Digite apenas números inteiros.')

    resp = requests.get(f"{API_URL}/clientes/{cliente_id}/pedidos")

    if resp.status_code == 200:
        pedidos = resp.json()
        if pedidos:
            print(f"\nPedidos encontrados para o cliente de ID {cliente_id}:")
            for pedido in pedidos:
                print(
                    f"ID: {pedido['id']} | Produto: {pedido['produto']} | Valor: R$ {pedido['valor']} | Data: {pedido['data']}")
        else:
            print(f"\nNenhum pedido foi encontrado para o cliente de ID {cliente_id}.")
    elif resp.status_code == 404:
        print("\n", resp.json().get('detail'))
    else:
        print("\nOcorreu um erro no servidor:")
        print("Código de Status:", resp.status_code)
        print("Mensagem:", resp.json())

def atualizar_cliente():
    print("\n--- ATUALIZAÇÃO DE CLIENTE ---")
    while True:
        cliente_id_input = input('ID do Cliente a ser atualizado: ').strip()
        if cliente_id_input.isdigit():
            cliente_id = int(cliente_id_input)
            break
        print("ID inválido. Por favor, digite um número.")

    nome = input('Novo Nome (deixe em branco para não alterar): ').strip()
    email = input('Novo Email (deixe em branco para não alterar): ').strip()
    telefone = input('Novo Telefone (deixe em branco para não alterar): ').strip()

    payload = {}
    if nome:
        payload['nome'] = nome
    if email:
        payload['email'] = email
    if telefone:
        payload['telefone'] = telefone

    resp = requests.patch(f"{API_URL}/clientes/{cliente_id}", json=payload)
    print("\nResposta do Servidor:", resp.json())


def excluir_cliente():
    print("\n--- EXCLUSÃO DE CLIENTE ---")
    while True:
        cliente_id_input = input('ID do Cliente a ser excluído: ').strip()
        if cliente_id_input.isdigit():
            cliente_id = int(cliente_id_input)
            break
        print("ID inválido. Por favor, digite um número.")

    resp = requests.delete(f"{API_URL}/clientes/{cliente_id}")
    if resp.status_code == 204:
        print("\nCliente deletado com sucesso!")
    else:
        print("\nErro ao deletar cliente:", resp.json())


def cadastrar_pedido():
    print("\n--- CADASTRO DE PEDIDO ---")
    while True:
        try:
            cliente_id = int(input('ID do Cliente: ').strip())
            break
        except ValueError:
            print("ID do Cliente inválido. Por favor, digite um número.")

    while True:
        produto = input('Produto: ').strip()
        if not produto:
            print("O nome do produto não pode ser vazio.")
            continue
        break

    while True:
        try:
            valor = float(input('Valor: '))
            if valor < 0:
                print("O valor deve ser igual ou maior que 0.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    resp = requests.post(f"{API_URL}/pedidos/adicionar", json={
        "cliente_id": cliente_id,
        "produto": produto,
        "valor": valor
    })
    print("\nResposta do Servidor:", resp.json())


def listar_pedidos():
    print("\n--- LISTA DE PEDIDOS ---")
    resp = requests.get(f"{API_URL}/pedidos/lista")
    resp.raise_for_status()

    pedidos = resp.json()
    if pedidos:
        print("\nPedidos encontrados:")
        for pedido in pedidos:
            print(
                f"ID: {pedido['id']} | Cliente ID: {pedido['cliente_id']} | Produto: {pedido['produto']} | Valor: R$ {pedido['valor']} | Data: {pedido['data']}")
    else:
        print("\nNenhum pedido foi encontrado.")


def atualizar_pedido():
    print("\n--- ATUALIZAÇÃO DE PEDIDO ---")
    while True:
        pedido_id_input = input('ID do Pedido a ser atualizado: ').strip()
        if pedido_id_input.isdigit():
            pedido_id = int(pedido_id_input)
            break
        print("ID inválido. Por favor, digite um número.")

    cliente_id = input('Novo ID do Cliente (deixe em branco para não alterar): ').strip()
    produto = input('Novo Produto (deixe em branco para não alterar): ').strip()
    valor = input('Novo Valor (deixe em branco para não alterar): ').strip()

    payload = {}
    if cliente_id:
        payload['cliente_id'] = int(cliente_id)
    if produto:
        payload['produto'] = produto
    if valor:
        payload['valor'] = float(valor)

    resp = requests.patch(f"{API_URL}/pedidos/{pedido_id}/atualizar", json=payload)
    print("\nResposta do Servidor:", resp.json())


def excluir_pedido():
    print("\n--- EXCLUSÃO DE PEDIDO ---")
    while True:
        pedido_id_input = input('ID do Pedido a ser excluído: ').strip()
        if pedido_id_input.isdigit():
            pedido_id = int(pedido_id_input)
            break
        print("ID inválido. Por favor, digite um número.")

    resp = requests.delete(f"{API_URL}/pedidos/{pedido_id}/deletar")
    if resp.status_code == 204:
        print("\nPedido deletado com sucesso!")
    else:
        print("\nErro ao deletar pedido:", resp.json())


def sair():
    print('Saindo do programa...')
    sys.exit()


def menu_escolhas():
    acoes = {
        '1': cadastrar_cliente,
        '2': listar_clientes,
        '3': listar_pedidos_de_cliente,
        '4': atualizar_cliente,
        '5': excluir_cliente,
        '6': cadastrar_pedido,
        '7': listar_pedidos,
        '8': atualizar_pedido,
        '9': excluir_pedido,
        '0': sair
    }

    while True:
        print('\n==============================MENU==================================')
        opcao = input('''
Digite o numero correspondente para escolher uma opção:
[1] Cadastrar Cliente
[2] Listar Clientes
[3] Listar Pedidos de um Cliente
[4] Atualizar Cliente
[5] Excluir Cliente
[6] Cadastrar Pedido
[7] Listar Pedidos
[8] Atualizar Pedido
[9] Excluir Pedido
[0] Sair
>>>>>> ''')

        try:
            if opcao in acoes:
                acoes[opcao]()
            else:
                print('Opção inválida. Tente novamente.')

        except requests.exceptions.ConnectionError:
            print(
                "\nERRO: Não foi possível conectar ao servidor. Verifique se sua API está rodando em http://127.0.0.1:8000.")
        except requests.exceptions.HTTPError as e:
            print(f"\nERRO HTTP: {e}")
        except ValueError as e:
            print(f"\nERRO: Um valor numérico inválido foi inserido. Detalhes: {e}")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == "__main__":
    menu_escolhas()