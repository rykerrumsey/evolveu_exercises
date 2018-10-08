import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_client_table = "CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name text, email text, phone text, payment_type text, payment_status text, issues text, notes text)"
cursor.execute(create_client_table)

connection.commit()
connection.close()
