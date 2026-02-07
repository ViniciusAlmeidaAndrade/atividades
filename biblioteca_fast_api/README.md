 # Biblioteca FastAPI 📚


API REST para gerenciamento de um acervo de livros, construída com **FastAPI**, um framework moderno, rápido e de alta performance para APIs em Python. :contentReference[oaicite:2]{index=2}


---


## 🚀 Visão Geral


Esta API permite:


- Cadastrar livros

- Listar livros existentes

- Consultar livro por ID

- Atualizar dados de um livro

- Remover livros


A intenção do projeto é praticar a criação de endpoints REST usando **FastAPI**, além de aplicar conceitos como validação de dados com Pydantic, rotas organizadas e uso de servidor ASGI (Uvicorn). :contentReference[oaicite:3]{index=3}


---


## 🧰 Tecnologias


| Tecnologia | Função |

|------------|--------|

| Python     | Linguagem principal |

| FastAPI    | Framework para criar a API REST |

| Uvicorn    | Servidor ASGI para rodar a aplicação |

| Pydantic   | Para validação e modelagem de dados |


> FastAPI é conhecido por ser altamente performático e por gerar documentação automática da API. :contentReference[oaicite:4]{index=4}


---


## 📁 Estrutura do Projeto


```text

biblioteca_fast_api/

├── app/

│   ├── main.py             # Ponto de entrada da API

│   ├── models.py           # Modelos de dados com Pydantic

│   ├── routes/             # Rotas da API

│   └── services/           # Lógica de negócio (CRUD)

├── requirements.txt        # Dependências do projeto

└── README.md               # Documentação deste projeto
```

(A estrutura acima assume uma organização típica — ajuste conforme a real do projeto.)

## 🛠️ Instalação


Clone o repositório

```
git clone https://github.com/ViniciusAlmeidaAndrade/atividades.git

cd atividades/biblioteca_fast_api
```

Crie e ative um ambiente virtual

```
python -m venv venv

source venv/bin/activate   # macOS/Linux

venv\Scripts\activate      # Windows
```

Instale as dependências

```
pip install -r requirements.txt
```

## ▶️ Como Executar


Inicie o servidor com:

```
uvicorn app.main:app --reload
```

> A API estará disponível em: http://127.0.0.1:8000


> A documentação interativa (Swagger UI): http://127.0.0.1:8000/docs


FastAPI já gera documentação automática para todos os endpoints com base nos models e rotas definidos.


## 🧪 Endpoints Principais

```
Método |  Endpoint      | Descrição

GET    |  /livros       | Lista todos os livros

GET    |  /livros/{id}  | Consulta livro por ID

POST   |  /livros       | Adiciona um novo livro

PUT    |  /livros/{id}  | Atualiza um livro

DELETE |  /livros/{id}  | Remove um livro
```
