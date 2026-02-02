# 💰 Financial Transactions API

API REST desenvolvida em **Python + FastAPI** para gerenciamento de transações financeiras, com persistência em **MySQL**, suporte a **CRUD completo**, **filtros**, **relatórios** e integração via **CLI e API**.

Projeto criado com foco em **boas práticas de backend**, organização em camadas e uso real de banco de dados relacional.

---

## 🚀 Funcionalidades

- ✅ Criar transações (entrada e saída)
- ✅ Listar transações
- ✅ Atualizar transações
- ✅ Deletar transações
- ✅ Filtro por tipo (`INCOME` / `EXPENSE`)
- ✅ Filtro por categoria
- ✅ Cálculo de saldo total
- ✅ Relatórios financeiros
- ✅ Integração com MySQL
- ✅ Documentação automática via Swagger

---

## 🧱 Arquitetura do Projeto

financial_transactions_sql/
│
├── api.py # API FastAPI
├── cli.py # Interface via terminal
├── services.py # Regras de negócio
├── reports.py # Relatórios financeiros
│
├── db/
│ ├── init.py
│ └── connection.py
│
├── requirements.txt
└── README.md

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **MySQL**
- **Uvicorn**
- **Pydantic**
- **mysql-connector-python**

---

## ▶️ Como rodar o projeto

### 1️⃣ Clone o repositório

git clone https://github.com/seu-usuario/financial-transactions-api.git
cd financial-transactions-api
2️⃣ Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Instale as dependências
pip install -r requirements.txt
4️⃣ Configure o banco de dados MySQL
Crie o banco:

CREATE DATABASE finance_manager;
Crie a tabela:

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10,2),
    category VARCHAR(100),
    type ENUM('INCOME','EXPENSE'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Configure suas credenciais em:

db/connection.py
▶️ Rodando a API

uvicorn api:app --reload
Acesse:

http://127.0.0.1:8000/docs
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