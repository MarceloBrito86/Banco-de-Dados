import mysql.connector # Importa o módulo mysql.connector para se conectar ao MySQL
from mysql.connector import Error # Importa a classe Error para tratamento de exceções

# Configuração do banco de dados
db_config = {
    'host': 'localhost', # Endereço do servidor MySQL
    'user': 'root', # Nome de usuário do MySQL
    'passwd': 'he182555@', # Senha do MySQL
    'database': 'crm_bank' # Nome do banco de dados a ser usado
}

# Função para criar conexão com o banco de dados
def create_connection(config):
    connection = None # Inicializa a variável connection como None
    try: # Tenta conectar ao banco de dados com as configurações fornecidas
        connection = mysql.connector.connect(**config)
        print("Connection to MySQL DB successful") # Imprime uma mensagem de sucesso se a conexão for estabelecida
    except Error as e: # Captura e imprime qualquer erro que ocorrer durante a conexão
        print(f"The error '{e}' occurred")
    return connection # Retorna a conexão (ou None se falhar)

# Criar a conexão
conn = create_connection(db_config) # Chama a função create_connection com as configurações do banco de dados
cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Criação do banco de dados e tabelas, e inserção de dados
create_db_and_tables = """
CREATE DATABASE IF NOT EXISTS crm_bank;
USE crm_bank;
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS opportunities (
    opportunity_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    value DECIMAL(10, 2),
    stage VARCHAR(50),
    close_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    contact_id INT,
    activity_type VARCHAR(50),
    subject VARCHAR(100),
    description TEXT,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE SET NULL
);

INSERT INTO customers (name, address, city, state, postal_code, country, phone, email)
VALUES ('Empresa Exemplo', 'Rua Exemplo, 123', 'Lisboa', 'Lisboa', '1000-000', 'Portugal', '211234567', 'contato@exemplo.com');

INSERT INTO contacts (customer_id, first_name, last_name, phone, email)
VALUES (1, 'João', 'Silva', '211234568', 'joao.silva@exemplo.com');

INSERT INTO opportunities (customer_id, name, description, value, stage, close_date)
VALUES (1, 'Projeto Exemplo', 'Descrição do projeto', 10000.00, 'Negociação', '2024-12-31');

INSERT INTO activities (customer_id, contact_id, activity_type, subject, description, due_date)
VALUES (1, 1, 'Reunião', 'Reunião inicial', 'Discutir detalhes do projeto', '2024-06-30');
"""

# Executar a criação do banco de dados e tabelas, e inserção de dados
for statement in create_db_and_tables.split(';'): # Divide os comandos SQL em declarações individuais
    if statement.strip(): # Ignora declarações vazias
        try:
            cursor.execute(statement)  # Executa cada declaração SQL
        except Error as e:
            print(f"The error '{e}' occurred while executing: {statement}") # Captura e imprime qualquer erro que ocorrer durante a execução

# Consultas para listar os dados
queries = [
    "SELECT * FROM customers", # Conculta para selecionar todos os dados da tabela customers
    "SELECT * FROM contacts", # Consulta para selecionar todos os dados da tabela contacts
    "SELECT * FROM opportunities", # Consulta para selecionar todos os dados da tabela opportunities
    "SELECT * FROM activities" # Consulta para selecionar todos os dados da tabela activities
]

# Executar as consultas e exibir os resultados
results = {}
for query in queries:
    cursor.execute(query) # Executa a consulta SQL
    results[query] = cursor.fetchall() # Armazena todos os resultados da consulta em um dicionário

# Fechar a conexão com o banco de dados
cursor.close() # Fecha o cursor
conn.close() # Fecha a conexão

# Exibir os resultados
for query, result in results.items(): # Itera sobre as consultas e seus resultados
    print(f"\nResults for query: {query}") # Imprime a consulta
    for row in result: # Itera as linhas de resultados
        print(row) # Imprime cada linha de resultado