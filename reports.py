from db.connection import get_connection

def get_reports():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        WHERE type = 'EXPENSE'
        GROUP BY category
    """)
    expenses_by_category = cursor.fetchall()

    cursor.execute("""
        SELECT type, SUM(amount) AS total
        FROM transactions
        GROUP BY type
    """)
    income_vs_expense = cursor.fetchall()

    cursor.execute("""
        SELECT description, amount, created_at
        FROM transactions
        WHERE type = 'EXPENSE'
        AND MONTH(created_at) = MONTH(CURRENT_DATE())
    """)
    current_month_expenses = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "expenses_by_category": expenses_by_category,
        "income_vs_expense": income_vs_expense,
        "current_month_expenses": current_month_expenses
    }
