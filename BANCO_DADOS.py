import sqlite3

banco = sqlite3.connect('Sistema de restaurantes.db')
cursor = banco.cursor()

# CLIENTES
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone INTEGER
)""")

cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('Raiane', 950883352)")
cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('Ana', 925132418)")
cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('Maria', 946739019)")
cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('João', 904536281)")
cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('Pedro', 924167936)")
cursor.execute("INSERT INTO clientes (nome, telefone) VALUES ('Lucas', 982647345)")

# PEDIDOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER,
    id_cliente INTEGER,
    data TEXT
)""")
cursor.execute("INSERT INTO pedidos VALUES(1, 2, '2025-10-19')")
cursor.execute("INSERT INTO pedidos VALUES(2, 4, '2025-11-20')")
cursor.execute("INSERT INTO pedidos VALUES(3, 1, '2025-12-21')")
cursor.execute("INSERT INTO pedidos VALUES(4, 5, '2026-01-22')")
cursor.execute("INSERT INTO pedidos VALUES(5, 3, '2026-02-23')")
cursor.execute("INSERT INTO pedidos VALUES(6, 6, '2026-03-24')")

# PRATOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS pratos (
    id INTEGER,
    nome TEXT,
    preco REAL
)""")
cursor.execute("INSERT INTO pratos VALUES(1, 'pizza', 30.00)")
cursor.execute("INSERT INTO pratos VALUES(2, 'hamburguer', 25.00)")
cursor.execute("INSERT INTO pratos VALUES(3, 'salada', 15.00)")
cursor.execute("INSERT INTO pratos VALUES(4, 'sushi', 40.00)")
cursor.execute("INSERT INTO pratos VALUES(5, 'lasanha', 35.00)")
cursor.execute("INSERT INTO pratos VALUES(6, 'churrasco', 50.00)")
cursor.execute("INSERT INTO pratos VALUES(7, 'feijoada', 28.00)")
cursor.execute("INSERT INTO pratos VALUES(8, 'tacos', 22.00)")
cursor.execute("INSERT INTO pratos VALUES(9, 'sanduiche', 18.00)")
cursor.execute("INSERT INTO pratos VALUES(10, 'macarrão', 27.00)")

# ITENS_PEDIDOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS itens_pedidos (
    id INTEGER,
    id_pedido INTEGER,
    id_prato INTEGER,
    quantidade INTEGER
)""")
cursor.execute("INSERT INTO itens_pedidos VALUES(1, 1, 5, 2)")
cursor.execute("INSERT INTO itens_pedidos VALUES(2, 2, 3, 1)")
cursor.execute("INSERT INTO itens_pedidos VALUES(3, 3, 7, 4)")
cursor.execute("INSERT INTO itens_pedidos VALUES(4, 4, 2, 6)")
cursor.execute("INSERT INTO itens_pedidos VALUES(5, 5, 6, 3)")
cursor.execute("INSERT INTO itens_pedidos VALUES(6, 6, 8, 5)")

# UPDATE
cursor.execute("UPDATE itens_pedidos SET quantidade = 10 WHERE id = 3")

# SELECT para visualizar
cursor.execute("SELECT * FROM itens_pedidos")
print(cursor.fetchall())

banco.commit()
banco.close()






UPDATE 
cursor.execute("UPDATE emprestimos SET data_devolucao = '22/02/2024' WHERE id = 3")
cursor.execute ("UPDATE livros SET ano_publicacao = 2021 WHERE id = 5")
OU SEJA UPDATE (NOME DA TABELA) SET (NOME DA COLUNA) = 'NOVO VALOR' WHERE (CONDICAO) NO CASO, ID = 3



SELECT 
cursor.execute("SELECT * FROM AUTORES")
print(cursor.fetchall())

cursor.execute("SELECT  nome_aluno,data_emprestimo, data_devolucao FROM EMPRESTIMOS WHERE nome_aluno = 'José de Alencar'")
OU SEJA, SELECIONA AS COLUNAS (NOME DA COLUNA) DA TABELA (NOME DA TABELA) ONDE (CONDICAO) NO CASO, NOME_ALUNO = 'JOSÉ DE ALENCAR'
cursor.execute("SELECT titulo, ano_publicacao FROM LIVROS WHERE ano_publicacao >= 2020")
OU SEJA, SELECIONA AS COLUNAS (NOME DA COLUNA) DA TABELA (NOME DA TABELA) ONDE (CONDICAO) NO CASO, ANO_PUBLICACAO >= 2020
print(cursor.fetchall())


DELETE 
cursor.execute("DELETE FROM EMPRESTIMOS WHERE id = 6")
OU SEJA, DELETA DA TABELA (NOME DA TABELA) ONDE (CONDICAO) NO CASO, ID = 6




































import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Tabela autores
cursor.execute('''
CREATE TABLE IF NOT EXISTS AUTORES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    nacionalidade TEXT
)
''')

# Tabela livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS LIVROS ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    ano_publicacao INTEGER,
    genero TEXT,
    FOREIGN KEY (autor_id) REFERENCES AUTORES(id)
)
''')

# Tabela emprestimos
cursor.execute('''
CREATE TABLE IF NOT EXISTS EMPRESTIMOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livro INTEGER,
    nome_aluno TEXT,
    data_emprestimo TEXT,
    data_devolucao TEXT,
    FOREIGN KEY (id_livro) REFERENCES LIVROS(id)
)
''')

# Inserindo autores
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('Valentina', 'Brasileira')")
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('Camila', 'Brasileira')")
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('Maria', 'Italiana')")
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('João','Espanhol')")
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('Pedro', 'Brasileiro')")
cursor.execute("INSERT INTO AUTORES (nome, nacionalidade) VALUES('Leticia', 'Brasileira')")

# Inserindo livros
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('Asas da Liberdade', 1, 2020, 'Romance')")
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('O Segredo do Tempo', 2, 2018, 'Ficção Científica')")
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('A Cidade dos Sonhos', 3, 2019, 'Fantasia')")
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('O Último Guardião', 4, 2021, 'Aventura')")
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('Divergente', 5, 2017, 'Distopia')")
cursor.execute("INSERT INTO LIVROS (titulo, autor_id, ano_publicacao, genero) VALUES('O Código da Vida', 6, 2022, 'Suspense')")

# Inserindo empréstimos
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(1, 'Clarice Lispector', '10/10/2023', '20/10/2023')")
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(2, 'Machado de Assis', '11/11/2023', '21/11/2023')")
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(3, 'Jorge Amado', '12/12/2023', '22/12/2023')")
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(4, 'Graciliano Ramos', '13/01/2024', '23/01/2024')")
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(5, 'Cecília Meireles', '14/02/2024', '24/02/2024')")
cursor.execute("INSERT INTO EMPRESTIMOS (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES(6,  'José de Alencar', '15/03/2024', '25/03/2024')")



# cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", ('30/10/2023', 1))









conn.commit()
conn.close()


