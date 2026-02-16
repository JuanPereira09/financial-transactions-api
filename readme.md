💰 Financial Transactions API

API REST desenvolvida em Python + FastAPI para gerenciamento de transações financeiras com autenticação JWT, persistência em MySQL, suporte a CRUD completo, filtros, relatórios e integração via CLI e API.
Projeto construído com foco em:
Boas práticas de backend
Organização em camadas (services, db, auth)
Autenticação segura com OAuth2 + JWT
Integração real com banco relacional

🚀 Funcionalidades
🔐 Autenticação

✅ Registro de usuários
✅ Login com OAuth2 Password Flow
✅ Hash seguro com bcrypt
✅ Geração de JWT
✅ Rotas protegidas com Bearer Token

💰 Transações

✅ Criar transações (entrada e saída)
✅ Listar transações
✅ Atualizar transações
✅ Deletar transações
✅ Filtro por tipo (INCOME / EXPENSE)
✅ Filtro por categoria
✅ Cálculo de saldo total
✅ Relatórios financeiros
✅ Transações vinculadas ao usuário autenticado

🧩 Extras
✅ Integração com MySQL
✅ Documentação automática via Swagger
✅ Interface via CLI

🧱 Arquitetura do Projeto
financial_transactions_sql/
│
├── api.py                # API FastAPI
├── cli.py                # Interface via terminal
├── services.py           # Regras de negócio
├── reports.py            # Relatórios financeiros
├── auth.py               # Autenticação e JWT
│
├── db/
│   ├── __init__.py
│   └── connection.py
│
├── requirements.txt
├── .gitignore
└── README.md

🛠️ Tecnologias Utilizadas

Python 3.11
FastAPI
MySQL
Uvicorn
Pydantic
Passlib (bcrypt)
Python-JOSE (JWT)
OAuth2PasswordBearer

mysql-connector-python

▶️ Como rodar o projeto
1️⃣ Clone o repositório
git clone https://github.com/JuanPereira09/financial-transactions-api.git
cd financial-transactions-api

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure o banco de dados MySQL

Crie o banco:
CREATE DATABASE finance_manager;

Crie a tabela de usuários:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

Crie a tabela de transações:

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

Configure suas credenciais em:

db/connection.py

▶️ Rodando a API
uvicorn api:app --reload

Acesse:
http://127.0.0.1:8000/docs

🔐 Fluxo de Autenticação

1️⃣ Registrar usuário
POST /register
{
  "username": "juan",
  "email": "juan@email.com",
  "password": "123456"
}

2️⃣ Login
POST /login

Use o botão 🔒 Authorize no Swagger e informe:

username
password

O sistema gera automaticamente o JWT.

3️⃣ Rotas protegidas
Exemplo:
GET /protected

Requer token Bearer válido.

🔎 Endpoints Principais
🔹 Listar transações
GET /transactions

🔹 Filtrar por tipo
GET /transactions?type=EXPENSE

🔹 Filtrar por categoria
GET /transactions?category=Alimentação

🔹 Criar transação
POST /transactions

{
  "description": "Academia",
  "amount": 150,
  "category": "Saúde",
  "type": "EXPENSE"
}

🔹 Atualizar transação
PUT /transactions/{id}

🔹 Deletar transação
DELETE /transactions/{id}

🔹 Ver saldo
GET /balance

🔹 Relatórios
GET /reports

🖥️ Uso via CLI
python cli.py list
python cli.py add
python cli.py balance
python cli.py report
