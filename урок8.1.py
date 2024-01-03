import sqlite3
from datetime import datetime, timedelta


conn = sqlite3.connect('bank.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        balance REAL NOT NULL DEFAULT 0
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        amount REAL NOT NULL,
        transaction_type TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES clients(id)
    )
''')

def register_client(full_name, phone_number):
    cursor.execute('INSERT INTO clients (full_name, phone_number) VALUES (?, ?)', (full_name, phone_number))
    conn.commit()


def find_client(search_param):
    cursor.execute('SELECT * FROM clients WHERE full_name LIKE ? OR phone_number = ?', ('%' + search_param + '%', search_param))
    return cursor.fetchall()


def deposit(client_id, amount):
    cursor.execute('UPDATE clients SET balance = balance + ? WHERE id = ?', (amount, client_id))
    cursor.execute('INSERT INTO transactions (client_id, amount, transaction_type) VALUES (?, ?, "deposit")', (client_id, amount))
    conn.commit()


def withdraw(client_id, amount):
    cursor.execute('UPDATE clients SET balance = balance - ? WHERE id = ?', (amount, client_id))
    cursor.execute('INSERT INTO transactions (client_id, amount, transaction_type) VALUES (?, ?, "withdraw")', (client_id, amount))
    conn.commit()


def view_balance(client_id):
    cursor.execute('SELECT balance FROM clients WHERE id = ?', (client_id,))
    return cursor.fetchone()[0]


def calculate_deposit(client_id, months):
    interest_rate = 5  
    principal = view_balance(client_id)
    for month in range(months):
        principal += principal * (interest_rate / 100)
    return principal


register_client("Иван Иванов", "1234567890")
client_id = find_client("Иван Иванов")[0][0]

deposit(client_id, 1000)
print(f"Баланс после пополнения: {view_balance(client_id)}")

withdraw(client_id, 500)
print(f"Баланс после снятия: {view_balance(client_id)}")

deposit(client_id, 200)
print(f"Баланс после еще одного пополнения: {view_balance(client_id)}")

months = 12
deposit_amount = calculate_deposit(client_id, months)
print(f"Сумма вклада через {months} месяцев: {deposit_amount}")


conn.close()
