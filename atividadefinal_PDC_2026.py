"""
Anotações:

modelo mental:

Imaginar um dicionário como um conjunto não-ordenado de chave:valor, 
onde as chaves são únicas em uma dada instância do dicionário.

Dicionários são delimitados por {} (Chaves), e contém uma lista de pares chave:valor
separado por vírgulas.


valor: onde 


"""

"""
Projeto 5 — Sistema de Gerenciamento de Mercadinho

Projeto de um “Mini Sistema de Mercadinho”

Descrição do Projeto:

O aluno deve criar um sistema de terminal que permita gerenciar produtos e realizar vendas
em um pequeno mercado, emitindo um cupom simplificado ao final.

=========================================================================================

Funcionalidades Obrigatórias:

1. Cadastro de Produtos:
• Armazenar produtos em um dicionário onde a chave é o código e o valor é outro
dicionário com nome, preço e estoque
• Permitir adicionar, editar e remover produtos

2. Realizar Venda:
• Montar um carrinho de compras usando lista
• Verificar se há estoque suficiente (condicional)
• Calcular o total e aplicar desconto se o valor for maior que R$ 100 (condicional +
numéricos)
• Atualizar o estoque após a venda (laço de repetição)

3. Emitir Cupom:
• Gerar cupom formatado com data/hora usando datetime (módulo builtin)
• Formatar valores monetários e alinhar o texto (strings e f-strings)

4. Relatórios:
• Listar produtos com estoque baixo (< 5 unidades)
• Mostrar o histórico de vendas do dia

5. Menu Interativo:
• Loop principal com opções (while + match/if)
• Validação de entrada do usuário

"""

# Código em construção:

import datetime
import os

pedido = {}
historico_vendas = []
produtos = {}


def cadastrar_produto():

    codigo = input("Digite o código: ")

    if codigo in produtos:
        print('Esse código já existe!')
        print("Comece tudo de novo!")
        return
        
    print("Deixe em branco para manter o valor atual.")
    nome = input(f"Nome ({produtos[codigo]['nome']}): ").strip()
    preco = input(f"Preço ({produtos[codigo]['preco']:.2f}): ").strip()
    estoque = input(f"Estoque ({produtos[codigo]['estoque']}): ").strip()
    if nome:
        produtos[codigo]['nome'] = nome
    if preco:
        try:
            produtos[codigo]['preco'] = float(preco)
        except ValueError:
            print(" Preço inválido, mantido o anterior.")
    if estoque:
        try:
            produtos[codigo]['estoque'] = int(estoque)
        except ValueError:
            print(" Estoque inválido, mantido o anterior.")
    print(" Produto atualizado!")


    # mostrar os produtos que já tem no sistema
    
    print(f'Produto: {nome}')
    print(f'Preço: {preco}')
    print(f'Estoque: {estoque}')
    return produtos

    print("*"*40)


def editar_produto():
    m = 10

def remover_produto():
    x = 7

def venda():

    carrinho = []

    if len(produtos) == 0:
        print("Cadastre produtos primeiro!")
        print("Pressione enter para continuar...")
        return
   

    while True:
        codigo = int(input("Digite o código do produto que deseja comprar: "))

        if codigo =='FIM':
            break

        if codigo not in produtos:
           print("Produto não cadastrado em nosso sistema!")
           continue

        produtos = produtos[codigo]
        # quantidade = 

    #     quantidade = int(input("Digite a quantidade: "))
    #     if quantidade <=0:
    #         print("quantidade insuficiente!")
    #         continue

    #     if quantidade > produtos[codigo]['estoque']:
    #         print("Estoque insuficiente!")
    #         continue

    #     subtotal = produtos[codigo]['preco'] * quantidade
    #     total2 += subtotal


    #     produtos[codigo]['estoque'] -= quantidade
    #     carrinho.append({'codigo':codigo, 'quantidade':quantidade, 'subtotal':subtotal})
    #     print(f"Subtotal: R${subtotal:.2f}")
    # print(f"Total da compra: R${total2:.2f}")
    # return carrinho, total2
    # X = 0


def desconto ():
    # desconto = compra /(100*10)
    # valor_final = desconto
    # return valor_final

    # print(f"Valor final: {valor_final:.2f}")
    V = 0

def relatorio_estoque_baixo():
    #@çx,ds.
    x = 0

def relatorio_historico():


# def

    print("*"*40)
compra()
desconto()

def menu():
    """Exibe o menu interativo e gerencia as opções."""
    while True:
        print("\n" + "="*40)
        print("        MERCADINHO - MENU")
        print("="*40)
        print("1. Cadastrar produto")
        print("2. Editar produto")
        print("3. Remover produto")
        print("4. Realizar venda")
        print("5. Relatórios")
        print("6. Sair")
        print("-"*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            editar_produto()
        elif opcao == '3':
            remover_produto()
        elif opcao == '4':
            compra()
        elif opcao == '5':
            # Submenu de relatórios
            print("\n--- Relatórios ---")
            print("1. Estoque baixo (<5)")
            print("2. Histórico de vendas do dia")
            sub = input("Escolha: ").strip()
            if sub == '1':
                relatorio_estoque_baixo()
            elif sub == '2':
                relatorio_historico()
            else:
                print("Opção inválida.")
        elif opcao == '6':
            print("Obrigado por usar o mercadinho! Até logo.")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 6.")

        input("\nPressione Enter para continuar...")

# ===== Inicialização com alguns produtos de exemplo =====
def popular_exemplos():
    """Adiciona alguns produtos de exemplo para teste."""
    exemplos = {
        '001': {'nome': 'Arroz', 'preco': 25.90, 'estoque': 10},
        '002': {'nome': 'Feijão', 'preco': 12.50, 'estoque': 8},
        '003': {'nome': 'Macarrão', 'preco': 5.75, 'estoque': 15},
        '004': {'nome': 'Leite', 'preco': 4.50, 'estoque': 3},  # estoque baixo
        '005': {'nome': 'Café', 'preco': 15.00, 'estoque': 2}    # estoque baixo
    }
    produtos.update(exemplos)

if __name__ == "__main__":
    popular_exemplos()   # já inicia com alguns produtos
    menu()
    






