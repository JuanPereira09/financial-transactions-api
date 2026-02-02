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
