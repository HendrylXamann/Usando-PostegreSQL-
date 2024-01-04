import psycopg2


def conectar():
    connection = psycopg2.connect(
        host="localhost",
        database="SecondBD",
        user="postgres",
        password="hahanãosubirnogit",
    )
    return connection
