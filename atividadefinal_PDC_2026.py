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
import random

print("\n")
print("*" * 40)
print("======== Bem vindo ao mercadinho ========")
print("*" * 40)
print("\n")
# Base de produtos:

pedido = {}
historico_vendas = []
produtos = {}

def cadastrar_produtos():
    codigo = input("Digite o código: ")
    if codigo in produtos:
        print('Esse código já existe!')
        print("Comece tudo de novo!")

    elif codigo not in produtos:
        nome =input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        estoque = int(input("Digite o estoque do produto: "))

    produtos['codigo'] =  {'nome': 'nome', 'preco':'preco', 'estoque': 'estoque'}

    # mostrar os produtos que já tem no sistema
    
    print(f'Produto: {nome}')
    print(f'Preço: {preco}')
    print(f'Estoque: {estoque}')
    return produtos

    print("*"*40)


def compra():

    carrinho = {}
    total = 0.0
    while True:
        codigo = int(input("Digite o código do produto que deseja comprar: "))

        if codigo == '000':
            break

        if codigo in produtos and estoque > 0:
            qtd = int(input("Digite a quantidade de produtos que quer comprar: "))
            cmp = codigo * qtd

            for i in produtos:
                total += cmp
                return cmp

        if codigo not in produtos:
           print("Produto não cadastrado em nosso sistema!")

           print(f"Total: R$ {total}")
        
        # if not carrinho:
        #     print("Compra não realizada! ")
        #     return

def desconto ():
    desconto = compra /(100*10)
    valor_final = desconto
    return valor_final
    print(f"Valor final: {valor_final:.2f}")



    print("*"*40)
cadastrar_produtos()
compra()

    # if codigo not in pedido:
    #     return "Digite um código válido"
    # else:
    #     carrinho += 1
    # total = len(carrinho)

# pedido = compra()
# print(pedido)
    







# def cupom():
#     if pedido > 100:
#         desconto = (pedido) - (100/10)
#         return desconto
#     valor_final = desconto

# cupom()

# def relatorio(pedidos, dia):



# def menu():
#     op = input()
#         "\n" + "="*40 + "\n"
#         "\n\n  Mercadinho\n" + "\n"
#         "\n" + "="*40 + "\n"
#         "\n1.Incluir  2.Tel+  3.Tel-  4.Excluir  5.Consultar  6.Listar  7.Salvar  8.Sair" + "\n"
#         "\nOpção: "

#     # )
#     return op

# def main():
#     carregar()
#     while True:
#         op = menu()
#         if op == '1': incluir_contato()
#         elif op == '2': incluir_telefone()
#         elif op == '3': excluir_telefone()
#         elif op == '4': excluir_contato()
#         elif op == '5': consultar_telefone()
#         elif op == '6': listar_contatos()
#         elif op == '7': salvar()
#         elif op == '8': salvar(); break
#         else: print("Inválido.")

# if __name__ == "__main__":
    # main()


# def nota_fiscal(pedido, hora):    