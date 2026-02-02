from reports import get_reports
from db.connection import get_connection

def get_all_transactions(tx_type=None, category=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM transactions WHERE 1=1"
    params = []

    if tx_type:
        query += " AND type = %s"
        params.append(tx_type)

    if category:
        query += " AND category = %s"
        params.append(category)

    query += " ORDER BY created_at DESC"

    cursor.execute(query, params)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_balance():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            SUM(CASE WHEN type = 'INCOME' THEN amount ELSE 0 END) -
            SUM(CASE WHEN type = 'EXPENSE' THEN amount ELSE 0 END)
            AS balance
        FROM transactions
    """)

    balance = cursor.fetchone()["balance"] or 0

    cursor.close()
    conn.close()

    return float(balance)

def get_reports():
    return {
        "expenses_by_category": expenses_by_category(),
        "income_vs_expense": income_vs_expense(),
        "current_month_expenses": current_month_expenses()
    }

def add_transaction(description, amount, category, tx_type):
    if tx_type not in ("INCOME", "EXPENSE"):
        raise ValueError("Tipo inválido. Use INCOME ou EXPENSE.")

    if amount <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (description, amount, category, type)
        VALUES (%s, %s, %s, %s)
    """, (description, amount, category, tx_type))

    conn.commit()
    cursor.close()
    conn.close()

def delete_transaction(transaction_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id = %s",
        (transaction_id,)
    )

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise ValueError("Transação não encontrada")

    conn.commit()
    cursor.close()
    conn.close()

def update_transaction(
    transaction_id: int,
    description: str,
    amount: float,
    category: str,
    tx_type: str
):
    if tx_type not in ("INCOME", "EXPENSE"):
        raise ValueError("Tipo inválido. Use INCOME ou EXPENSE.")

    if amount <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET description = %s,
            amount = %s,
            category = %s,
            type = %s
        WHERE id = %s
    """, (description, amount, category, tx_type, transaction_id))

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise ValueError("Transação não encontrada")

    conn.commit()
    cursor.close()
    conn.close()
