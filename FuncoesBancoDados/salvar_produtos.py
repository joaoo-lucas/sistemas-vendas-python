import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

def adicionar_produto(codigo, produto, data, valor, estoque):
    conexao = sqlite3.connect('estoque.db')
    cursor.execute("INSERT INTO estoque (Codigo, Produto, DataCadastro, ValorUnitario, Estoque) VALUES (?, ?, ?, ?, ?)", 
               (codigo, produto, data, valor, estoque))
    conexao.commit()
    conexao.close()

def consultar_produto(codigo):
    conexao = sqlite3.connect('estoque.db')
    cursor.execute("SELECT * FROM estoque WHERE Codigo = ?", (codigo,))
    produto = cursor.fetchone()
    return produto

def consultar_estoque():
    conexao = sqlite3.connect('estoque.db')
    cursor.execute("SELECT * FROM estoque")
    estoque = cursor.fetchall()
    print(estoque)

def excluir_produto(codigo):
    conexao = sqlite3.connect('estoque.db')
    cursor.execute("DELETE FROM estoque WHERE Codigo = ?", (codigo,))
    conexao.commit()



