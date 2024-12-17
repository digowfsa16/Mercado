from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('-------------------')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O Produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('        Listagem de produtos             ')
        print('-----------------------------------------')

        for produto in produtos:
            print(produto)
            print('.-')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_Produto() -> None:

    if len(produtos) > 0:  # Checa a existencia de produtos
        print('informe o código do produto que deseja adicionar ao carrinho')
        print('------------------------------------------------------------')
        print('=================== Produtos disponiveis ===================')
        for produto in produtos:
            print(produto)
            print('.-')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = get_produto_codigo(codigo)

        if produto:  # Se a função get_produto_codigo retornou um produto - executa
            if len(carrinho) > 0:   # Verifica se o carrinho ja tem produto ( caso tenha só adicionar a quantidade )
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O Produto {produto.nome} foi atualizado para {item.get(produto)} Unidades ')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    item = {produto: 1}
                    carrinho.append(item)
                    print(f'O Produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()

            else:  # Ação quando é um carrinho novo.
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:  # Se a função get_produto_codigo não retornou um produto
            print(f'Código {codigo} não existe')
            sleep(2)
            menu()
    else:  # Checa a existencia de produtos - Não existe
        print('Favor Cadastrar Produtos')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')
        print('--------------------')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('.-')
                sleep(1)

    else:
        print('Carrinho vazio')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quandidade: {dados[1]}')
                valor_total += float(dados[0].preco) * int(dados[1])
                print('--------------------------------------------')
                sleep(1)
        print(f'Sua Fatura é: {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(3)
    else:
        print('Carrinho vazio')
    sleep(2)
    menu()


def get_produto_codigo(codigo: int) -> Produto:
    prod: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            prod = produto
    return prod


def main() -> None:
    menu()


def menu() -> None:
    print('-------------------------------------------')
    print('=============== Bem-vindo(a) ==============')
    print('================ Py-Mercado ===============')
    print('-------------------------------------------')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_Produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida!')
        sleep(1)
        menu()


if __name__ == '__main__':
    main()
