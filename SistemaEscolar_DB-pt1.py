import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="he182555@",
    database="SistemaEscolar_DB"
)

# Criando um cursor
cursor = conn.cursor()

print("Conectado ao banco de dados!")

def adicionar_estudante(nome, data_nascimento, endereco, telefone, email):
    sql = "INSERT INTO Estudantes (nome, data_nascimento, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, data_nascimento, endereco, telefone, email)
    cursor.execute(sql, valores)
    conn.commit()
    print("Estudante adicionado com sucesso!")

def listar_estudantes():
    cursor.execute("SELECT * FROM Estudantes")
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)

def atualizar_estudante(id, nome, data_nascimento, endereco, telefone, email):
    sql = "UPDATE Estudantes SET nome = %s, data_nascimento = %s, endereco = %s, telefone = %s, email = %s WHERE id = %s"
    valores = (nome, data_nascimento, endereco, telefone, email, id)
    cursor.execute(sql, valores)
    conn.commit()
    print("Estudante atualizado com sucesso!")

def deletar_estudante(id):
    sql = "DELETE FROM Estudantes WHERE id = %s"
    valores = (id,)
    cursor.execute(sql, valores)
    conn.commit()
    print("Estudante deletado com sucesso!")

if __name__ == "__main__":
    # Adicionar um estudante
    adicionar_estudante('Pedro Oliveira', '2007-08-15', 'Rua E, 111', '95555-5555', 'pedro@example.com')
    
    # Listar todos os estudantes
    print("Lista de Estudantes:")
    listar_estudantes()
    
    # Atualizar um estudante
    atualizar_estudante(1, 'João Silva Atualizado', '2005-03-15', 'Rua A, 123', '99999-9999', 'joao_updated@example.com')
    
    # Deletar um estudante
    deletar_estudante(2)
    
    # Listar todos os estudantes novamente
    print("Lista de Estudantes após atualizações:")
    listar_estudantes()
    
    # Fechar a conexão
    cursor.close()
    conn.close()