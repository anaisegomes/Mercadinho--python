import datetime
import os

# ===== Estruturas de dados =====
produtos = {}          # {codigo: {'nome': str, 'preco': float, 'estoque': int}}
historico_vendas = []  # lista de dicionários com data, itens, total, desconto, final

# ===== Funções de cadastro =====
def cadastrar_produto():
    """Adiciona um novo produto ao estoque."""
    codigo = input("Código do produto: ").strip()
    if codigo in produtos:
        print("❌ Código já existe!")
        return
    nome = input("Nome: ").strip()
    try:
        preco = float(input("Preço (R$): "))
        estoque = int(input("Quantidade em estoque: "))
    except ValueError:
        print("❌ Valor inválido. Operação cancelada.")
        return
    produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque}
    print(f"✅ Produto '{nome}' cadastrado com sucesso!")

def editar_produto():
    """Edita os dados de um produto existente."""
    codigo = input("Código do produto a editar: ").strip()
    if codigo not in produtos:
        print("❌ Produto não encontrado!")
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
            print("❌ Preço inválido, mantido o anterior.")
    if estoque:
        try:
            produtos[codigo]['estoque'] = int(estoque)
        except ValueError:
            print("❌ Estoque inválido, mantido o anterior.")
    print("✅ Produto atualizado!")

def remover_produto():
    """Remove um produto do estoque."""
    codigo = input("Código do produto a remover: ").strip()
    if codigo not in produtos:
        print("❌ Produto não encontrado!")
        return
    confirm = input(f"Tem certeza que deseja remover '{produtos[codigo]['nome']}'? (s/N): ").lower()
    if confirm == 's':
        del produtos[codigo]
        print("✅ Produto removido!")
    else:
        print("Operação cancelada.")

# ===== Função de venda =====
def realizar_venda():
    """Processa uma venda: monta carrinho, calcula total, aplica desconto, atualiza estoque."""
    carrinho = []          # lista de {'codigo': str, 'nome': str, 'qtd': int, 'subtotal': float}
    total = 0.0

    print("\n--- Nova Venda ---")
    while True:
        codigo = input("Código do produto (ou '000' para finalizar): ").strip()
        if codigo == '000':
            break
        if codigo not in produtos:
            print("❌ Produto não cadastrado!")
            continue
        try:
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("❌ Digite um número válido.")
            continue

        if qtd <= 0:
            print("❌ Quantidade deve ser positiva.")
            continue
        if qtd > produtos[codigo]['estoque']:
            print(f"❌ Estoque insuficiente! Temos apenas {produtos[codigo]['estoque']} unidades.")
            continue

        # Calcula subtotal e adiciona ao carrinho
        subtotal = produtos[codigo]['preco'] * qtd
        carrinho.append({
            'codigo': codigo,
            'nome': produtos[codigo]['nome'],
            'qtd': qtd,
            'subtotal': subtotal
        })
        total += subtotal
        # Atualiza estoque
        produtos[codigo]['estoque'] -= qtd
        print(f"✅ Adicionado: {qtd}x {produtos[codigo]['nome']} - Subtotal: R${subtotal:.2f}")

    if not carrinho:
        print("Carrinho vazio. Venda cancelada.")
        return

    # Aplica desconto de 10% se total > 100
    desconto = 0.0
    if total > 100:
        desconto = total * 0.10
        print(f"🎉 Desconto de 10% aplicado: -R${desconto:.2f}")

    valor_final = total - desconto

    # Registra a venda no histórico
    venda = {
        'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        'itens': carrinho.copy(),
        'total': total,
        'desconto': desconto,
        'final': valor_final
    }
    historico_vendas.append(venda)

    # Emite o cupom
    emitir_cupom(venda)
    print("✅ Venda finalizada com sucesso!")

# ===== Emissão do cupom =====
def emitir_cupom(venda):
    """Gera e exibe o cupom fiscal formatado."""
    print("\n" + "="*50)
    print("         CUPOM FISCAL")
    print("="*50)
    print(f"Data/Hora: {venda['data']}")
    print("-"*50)
    print(f"{'Item':<20} {'Qtd':>5} {'Preço':>10} {'Subtotal':>12}")
    print("-"*50)
    for item in venda['itens']:
        # formatação alinhada
        print(f"{item['nome'][:20]:<20} {item['qtd']:>5} "
              f"R${produtos[item['codigo']]['preco']:>8.2f} "
              f"R${item['subtotal']:>10.2f}")
    print("-"*50)
    print(f"{'Total bruto:':<40} R${venda['total']:>8.2f}")
    if venda['desconto'] > 0:
        print(f"{'Desconto:':<40} -R${venda['desconto']:>7.2f}")
    print(f"{'Valor final:':<40} R${venda['final']:>8.2f}")
    print("="*50 + "\n")

# ===== Relatórios =====
def relatorio_estoque_baixo():
    """Lista produtos com estoque menor que 5 unidades."""
    print("\n--- Produtos com estoque baixo (<5) ---")
    encontrou = False
    for codigo, dados in produtos.items():
        if dados['estoque'] < 5:
            print(f"Código: {codigo} | {dados['nome']} | Estoque: {dados['estoque']}")
            encontrou = True
    if not encontrou:
        print("✅ Nenhum produto com estoque baixo.")

def relatorio_historico():
    """Mostra todas as vendas realizadas no dia atual."""
    hoje = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"\n--- Histórico de vendas do dia {hoje} ---")
    vendas_hoje = [v for v in historico_vendas if v['data'].startswith(hoje)]
    if not vendas_hoje:
        print("Nenhuma venda registrada hoje.")
        return
    for i, venda in enumerate(vendas_hoje, 1):
        print(f"\nVenda #{i} - {venda['data']}")
        print(f"  Itens: {len(venda['itens'])}")
        print(f"  Total: R${venda['total']:.2f} | Desconto: R${venda['desconto']:.2f} | Final: R${venda['final']:.2f}")

# ===== Menu principal =====
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
            realizar_venda()
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
                print("❌ Opção inválida.")
        elif opcao == '6':
            print("Obrigado por usar o mercadinho! Até logo.")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 6.")

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