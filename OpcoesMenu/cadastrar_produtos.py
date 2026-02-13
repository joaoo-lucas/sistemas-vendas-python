# Aqui você consegue cadastrar os produtos
import random
import main
from datetime import datetime
import FuncoesBancoDados.salvar_produtos as salvar_produtos

def cadastrar():
    produto = input('Produto: ')
    codigo  = random.randint(1000, 30000)
    estoque = int(input('Estoque: '))
    preco_unitario = float(input('Preço Unitário: '))
    data_cadastro = datetime.now()
    data_cadastro = data_cadastro.strftime('%d/%m/%Y')
    print(f'\nProduto cadastrado com sucesso!\n Produto: {produto}\n Código: {codigo}\n Estoque: {estoque}\n Preço Unitário: R$ {preco_unitario}\n Data do Cadastro: {data_cadastro}')
    salvar_produtos.adicionar_produto(codigo, produto, data_cadastro, preco_unitario, estoque)
    main.menu_principal()


    