import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="juan13sql09",
        database="finance_manager"
    )
