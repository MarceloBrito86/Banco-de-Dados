import mysql.connector # Importa a biblioteca mysql.connector  
from mysql.connector import Error # Classe Error para tratar possíveis erros de conexão e execução de consultas.

def create_connection(host_name, user_name, user_password, db_name):
    connection = None # Inicializa a variavel conexao como nula
    try: # Esta função tenta estabelecer uma conexão com o banco de dados usando os parâmetros fornecidos:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="he182555@",
            database="ecommerce"
        )
        print("Connection to MySQL DB successful") 
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection # Retorna a conexão estabelecida ou None em caso de falha

def execute_query(connection, query):# é usada para executar essa consulta e recuperar os resultados, que são então iterados e impressos na tela.
    cursor = connection.cursor() # Cria um cursor para executar comandos SQL na conexão fornecida
    try:
        cursor.execute(query) # é usada para executar essa consulta e realizar a inserção no banco de dados.
        connection.commit() # Confirma a transação no banco de dados
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query): 
    cursor = connection.cursor() # Cria um cursor para executar comandos SQL na conexão fornecida
    result = None # Inicializa a variável de resultado como nula
    try:
        cursor.execute(query) # Executa a consulta SQL passada como argumento
        result = cursor.fetchall() # Recupera todos os resultados da consulta
        return result # Retorna os resultados da consulta
    except Error as e:
        print(f"The error '{e}' occurred") # Se ocorrer um erro durante a execução da consulta, imprime a mensagem de erro

# Conectando ao banco de dados
connection = create_connection("localhost", "root", "your_password", "ecommerce")
# Chama a função create_connection para conectar ao banco de dados "ecommerce" no localhost usando usuário e senha 

# Executando uma consulta de leitura (selecionar todos os produtos)
select_products = "SELECT * FROM products" # Define a consulta SQL para selecionar todos os produtos da tabela "products"
products = execute_read_query(connection, select_products) # Executa a consulta de leitura e armazena os resultados em "products"

for product in products: # Itera sobre os produtos retornados pela consulta
    print(product) # Imprime cada produto

# Executando uma consulta de escrita (inserir um novo produto)
insert_product_query = """
INSERT INTO products (name, description, price, stock) VALUES 
('Smartwatch', 'Smartwatch com múltiplas funções', 300.00, 50)
"""
execute_query(connection, insert_product_query)
# Define a consulta SQL para inserir um novo produto na tabela "products" e a executa usando a função execute_query

# Fechando a conexão
if connection.is_connected(): # Verifica se a conexão está aberta
    connection.close() # Fecha a conexão com o banco de dados
    print("The connection is closed") # Imprime uma mensagem indicando que a conexão foi fechada