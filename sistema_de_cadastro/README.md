# 📖 Sistema de Gestão de Clientes e Pedidos

## 📌 Sobre o projeto
Este sistema é composto por:
- **API (FastAPI)** para cadastro, listagem, atualização e exclusão de clientes e pedidos.
- **Menu em terminal (CLI)** que funciona como cliente da API, permitindo interação via linha de comando.

O objetivo é facilitar a gestão de clientes e pedidos em um banco de dados **SQLite** de forma simples e intuitiva.

---

## ⚙️ Tecnologias usadas
- Python 3.12+
- FastAPI
- SQLite
- SQLAlchemy (assíncrono)
- Uvicorn
- Requests

---

## 📂 Estrutura do projeto
```text
.
├── main.py              # Inicializa o servidor FastAPI
├── menu.py              # Interface em terminal (cliente da API)
├── models.py            # Modelos de banco de dados (Cliente, Pedido)
├── schemas.py           # Schemas (Pydantic) para validação e resposta
├── routes_cliente.py    # Rotas relacionadas a clientes
├── routes_pedido.py     # Rotas relacionadas a pedidos
├── db.py                # Configuração do banco de dados SQLite
├── settings.py          # Configuração da aplicação FastAPI
├── cliente_pedido.sqlite3 # Banco de dados SQLite
└── requirements.txt     # Dependências do projeto
```

---

## 🔧 Instalação
Clone o repositório e entre na pasta do projeto:
```bash
git clone <seu-repositorio>
cd <pasta-do-projeto>
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar o sistema
O sistema deve ser executado em **dois terminais separados**:

### 1. Rodar o servidor FastAPI
```bash
uvicorn main:app --reload
```

O servidor ficará ativo em:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentação automática:
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. Rodar o menu no terminal
```bash
python menu.py
```

---

## 🖥️ Funcionalidades do Menu
```text
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
```

Cada opção faz uma requisição à API e mostra a resposta no terminal.

---

## 💾 Banco de Dados
- Banco usado: **SQLite** (`cliente_pedido.sqlite3`)  
- As tabelas são criadas automaticamente na primeira execução do servidor.  

---

## 📌 Observações
- Sempre inicie o **servidor FastAPI antes do menu**.  
- Se ocorrer erro de conexão no menu, verifique se a API está ativa em `http://127.0.0.1:8000`.  
