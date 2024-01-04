import ConnectingBD
import sys

db_config = ConnectingBD.conectar()


def inserir(connection, nome, validade, valor, qtdquestoes):
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO pythoncertificacoes (nome, validade, valor, qtdquestoes)
        VALUES (%s, %s, %s, %s)
        """,
        (nome, validade, valor, qtdquestoes),
    )
    connection.commit()


def exibir_formulario(nome, validade, valor, qtdquestoes):
    connection = db_config()
    inserir(connection, nome, validade, valor, qtdquestoes)
    connection.close()


# Script chamado por uma interface em Java que passa os valores para estas variáveis
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python script.py <nome> <validade> <valor> <qtdquestoes>")
        sys.exit(1)

    nome = sys.argv[1]
    validade = sys.argv[2]
    valor = sys.argv[3]
    qtdquestoes = sys.argv[4]

    exibir_formulario(nome, validade, valor, qtdquestoes)
