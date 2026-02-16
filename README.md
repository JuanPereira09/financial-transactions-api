💰 Financial Transactions API

Backend REST desenvolvido com Python + FastAPI para gerenciamento de transações financeiras com autenticação JWT e persistência em MySQL.

Projeto focado em arquitetura organizada, segurança e boas práticas de desenvolvimento backend.

🚀 Funcionalidades
🔐 Autenticação

Registro de usuários

Login com OAuth2 Password Flow

Hash de senha com bcrypt

Geração de JWT

Rotas protegidas com Bearer Token

💳 Transações

Criar transações (INCOME / EXPENSE)

Listar transações do usuário autenticado

Atualizar transações

Deletar transações

Filtro por tipo

Filtro por categoria

Cálculo automático de saldo

Relatórios financeiros

🧩 Extras

Integração com MySQL

Documentação automática via Swagger

Interface alternativa via CLI

🧱 Estrutura do Projeto
financial_transactions_sql/
│
├── api.py
├── auth.py
├── services.py
├── reports.py
├── cli.py
│
├── db/
│   ├── __init__.py
│   └── connection.py
│
├── requirements.txt
└── README.md

🛠 Tecnologias Utilizadas

Python 3.11

FastAPI

MySQL

Uvicorn

Pydantic

Passlib (bcrypt)

Python-JOSE (JWT)

OAuth2PasswordBearer

mysql-connector-python

▶️ Como Executar
1️⃣ Clonar repositório
git clone https://github.com/JuanPereira09/financial-transactions-api.git
cd financial-transactions-api

2️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar banco MySQL
CREATE DATABASE finance_manager;


Tabela de usuários:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);


Tabela de transações:

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10,2),
    category VARCHAR(100),
    type ENUM('INCOME','EXPENSE'),
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

▶️ Rodar API
uvicorn api:app --reload


Acessar documentação:

http://127.0.0.1:8000/docs

🔐 Fluxo de Autenticação

Registrar usuário:

POST /register

Login:

POST /login

Após login, usar botão 🔒 Authorize no Swagger.

📌 Endpoints Principais
Método	Endpoint	Descrição
GET	/transactions	Lista transações
POST	/transactions	Cria transação
PUT	/transactions/{id}	Atualiza transação
DELETE	/transactions/{id}	Remove transação
GET	/balance	Retorna saldo
GET	/reports	Relatório financeiro
🖥 Uso via CLI
python cli.py list
python cli.py add
python cli.py balance
python cli.py report
