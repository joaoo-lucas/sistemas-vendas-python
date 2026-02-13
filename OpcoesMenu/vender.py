# Aqui é onde se vende os produtos
import random
import FuncoesBancoDados.salvar_produtos as salvar_produtos

def carrinho():
    codigo = int(input('Codigo: '))
    produto = salvar_produtos.consultar_produto(codigo)
    while produto is None:
        print('\nProduto não existente!\n')
        codigo = int(input('Digite outro código: '))
        produto = salvar_produtos.consultar_produto(codigo)
    
    estoque = produto[4]
    nome = produto[1]
    preco = produto[3]
    quantia = int(input('Quantidade: '))
    
    while quantia <= 0 or quantia > estoque:
        print('\nQuantia inválida.\n')
        quantia = int(input('Quantidade: '))
    
    preco_total = quantia * preco
    print(f'Código: {codigo} \nProduto: {nome}\nPreço Unitário: R$ {preco:.2f}\nQuantidade no Estoque: {estoque}\nPreço Final: R$ {preco_total:.2f}')
    return {"Produto": nome, "Quantia": quantia, "Preço Final": preco_total}


def orcamento():
    cliente = input('Nome do cliente: ')
    telefone = input('Telefone: ')
    numero = random.randint(1000, 20000)
    lista_compra = []
    preco_total = 0
    while True:
        produtos = carrinho()
        lista_compra.append(f'{produtos['Quantia']}x {produtos['Produto']} - R$ {produtos['Preço Final']:.2f}')
        preco_total += produtos['Preço Final']
        continuar = input('Adicionar mais itens na sacola? (S/N) ')
        if continuar == 'n':
            break
        if continuar == 'N':
            break
    print(f'\nCliente: {cliente}\n\nItens da Lista')
    for produtos in lista_compra:
        print(f' - {produtos}')
    print(f'\nValor Final: R$ {preco_total:.2f}')
orcamento()