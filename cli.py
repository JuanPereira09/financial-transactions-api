import sys
from services import (
    get_all_transactions,
    get_balance,
    get_reports,
    add_transaction
)

def show_help():
    print("""
📌 COMANDOS DISPONÍVEIS:

python main.py list       → Lista todas as transações
python main.py balance    → Mostra o saldo atual
python main.py report     → Mostra relatórios financeiros
""")

def list_transactions():
    print("TRANSAÇÕES")
    for t in get_all_transactions():
        print(t)

def show_balance():
    print(f" Saldo atual: R$ {get_balance():.2f}")

def show_reports():
    reports = get_reports()

    print("\n GASTOS POR CATEGORIA")
    for r in reports["expenses_by_category"]:
        print(f"{r['category']}: R$ {r['total']}")

    print("\n ENTRADAS vs SAÍDAS")
    for r in reports["income_vs_expense"]:
        print(f"{r['type']}: R$ {r['total']}")

    print("\n GASTOS DO MÊS ATUAL")
    for r in reports["current_month_expenses"]:
        print(f"{r['description']} - R$ {r['amount']} ({r['created_at']})")

def add_transaction_cli():
    description = input("Descrição: ")
    amount = float(input("Valor: "))
    category = input("Categoria: ")
    tx_type = input("Tipo (INCOME / EXPENSE): ").upper()

    try:
        add_transaction(description, amount, category, tx_type)
        print("Transação adicionada com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    command = sys.argv[1].lower()

    if command == "list":
        list_transactions()
    elif command == "balance":
        show_balance()
    elif command == "report":
        show_reports()
    elif command == "add":
        add_transaction_cli()
    else:
        print("Comando inválido")
        show_help()