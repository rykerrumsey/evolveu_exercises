import psycopg2

def runSQL(query_string):
    conn = psycopg2.connect("dbname='postgres' \
        user='postgres' \
        host='172.18.0.2' \
        password='chonga' \
        port='5432'")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute(query_string)

    return cur.fetchall()
