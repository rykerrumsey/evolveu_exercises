import psycopg2

def main():
    try:
        conn = psycopg2.connect("dbname=postgres host=localhost user=postgres")
    except:
        print("I am unable to connect to the database")

main()
