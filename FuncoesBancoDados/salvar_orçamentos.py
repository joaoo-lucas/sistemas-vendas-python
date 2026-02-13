import sqlite3

conexao = sqlite3.connect('orcamentos.db')
cursor = conexao.cursor()

cursor.execute(

'''
    CREATE TABLE IF NOT EXISTS orcamentos (
        Numero INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeCliente TEXT,
        Itens TEXT,
        PrecoTotal REAL,
        DataOrçamento TEXT
    )
''')

def gerar_orçamento( numero ,nomecliente, data, precofinal, itens):
    conexao = sqlite3.connect('orcamento.db')
    cursor.execute("INSERT INTO orcamento (Numero, NomeCliente, Itens, PrecoTotal, DataOrçamento) VALUES (?, ?, ?, ?, ?)", 
               (numero, nomecliente, itens, precofinal, data))
    conexao.commit()
    conexao.close()