import main
import FuncoesBancoDados.salvar_produtos as salvar_produtos

def estoque():
    salvar_produtos.consultar_estoque()
    main.menu_principal()