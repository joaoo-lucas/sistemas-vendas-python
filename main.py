# Começo do código - aqui você pode escolher o que fazer;

import OpcoesMenu.cadastrar_produtos as cadastrar_produtos
import OpcoesMenu.estoque as estoque

def menu_principal():
    acao = int(input('\nO que você deseja fazer?\n 1. Cadastrar um produto \n 2. Acessar últimas vendas \n 3. Vender \n 4. Consultar estoque \n '))
    if acao == 1:
        cadastrar_produtos.cadastrar()
        return
    if acao == 4:   
        estoque.estoque()
        return

if __name__ == "__main__":
    menu_principal()