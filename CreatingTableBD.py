import ConnectingBD
# Função de conexão criada em outro arquivo
db_config = ConnectingBD.conectar()

# Cursor p/ executar o código SQL
cursor = db_config.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS pythoncertificacoes (
        id SERIAL PRIMARY KEY, 
        nome VARCHAR(100),
        validade DATE,
        valor FLOAT,
        qtdquestoes INTEGER  
    );
'''
# 'Serial' é sintaxe do postegres para autoincrement
cursor.execute(create_table_query)
db_config.commit()
db_config.close()
