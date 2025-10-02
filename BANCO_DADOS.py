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
