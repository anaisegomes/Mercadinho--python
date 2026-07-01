# ============================================
# PROJETO: SISTEMA DE GERENCIAMENTO DE MERCADINHO
# VERSÃO SUPER SIMPLIFICADA PARA INICIANTES
# ============================================

# Primeiro, importamos a biblioteca de data/hora
# (já vem instalada no Python, não precisa baixar nada)
from datetime import datetime

# ============================================
# NOSSOS "BANCOS DE DADOS" (guardamos na memória)
# ============================================

# Dicionário para guardar os produtos
# Exemplo: "001" -> {"nome": "Arroz", "preco": 5.00, "estoque": 10}
produtos = {}

# Lista para guardar o histórico de vendas
historico_vendas = []

# ============================================
# FUNÇÕES BÁSICAS DE AJUDA
# ============================================

def mostrar_dinheiro(valor):
    """Transforma um número em formato de dinheiro: R$ 10.00"""
    return f"R$ {valor:.2f}"

def pedir_numero(mensagem):
    """Pede um número para o usuário e não aceita letras"""
    while True:  # Fica repetindo até o usuário digitar certo
        try:
            # Tenta transformar o que o usuário digitou em número
            numero = float(input(mensagem))
            if numero > 0:  # Se for positivo, tá ok
                return numero
            else:
                print("Digite um número maior que zero!")
        except:
            # Se deu erro (usuário digitou letra), mostra mensagem
            print("Isso não é um número! Tente de novo.")

def pedir_inteiro(mensagem):
    """Pede um número inteiro (sem vírgula) para o usuário"""
    while True:
        try:
            numero = int(input(mensagem))
            if numero > 0:
                return numero
            else:
                print("Digite um número maior que zero!")
        except:
            print("Digite apenas números inteiros!")

# ============================================
# 1. FUNÇÕES PARA CADASTRAR PRODUTOS
# ============================================

def adicionar_produto():
    """Adiciona um novo produto no sistema"""
    print("\n" + "="*50)
    print("           ADICIONAR NOVO PRODUTO")
    print("="*50)
    
    # Pede o código do produto
    codigo = input("Digite o código do produto: ").strip()
    
    # Verifica se o código já existe
    if codigo in produtos:
        print("ERRO: Este código já existe!")
        input("Pressione Enter para voltar...")
        return
    
    # Pede os dados do produto
    nome = input("Nome do produto: ").strip()
    preco = pedir_numero("Preço unitário R$: ")
    estoque = pedir_inteiro("Quantidade em estoque: ")
    
    # Cria um dicionário com os dados do produto
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    
    # Salva no dicionário de produtos
    produtos[codigo] = produto
    
    print(f"\nProduto '{nome}' cadastrado com sucesso!")
    input("Pressione Enter para continuar...")

def editar_produto():
    """Modifica um produto que já existe"""
    print("\n" + "="*50)
    print("           EDITAR PRODUTO")
    print("="*50)
    
    # Mostra todos os produtos para o usuário escolher
    if len(produtos) == 0:
        print("Não tem nenhum produto cadastrado!")
        input("Pressione Enter para voltar...")
        return
    
    mostrar_produtos()
    
    # Pede o código do produto que quer editar
    codigo = input("\nDigite o código do produto que quer editar: ").strip()
    
    # Verifica se o produto existe
    if codigo not in produtos:
        print("Produto não encontrado!")
        input("Pressione Enter para continuar...")
        return
    
    # Pega o produto que será editado
    produto = produtos[codigo]
    print(f"\nEditando: {produto['nome']}")
    
    # Pergunta o que quer mudar
    print("\nDeixe em branco se não quiser mudar:")
    
    novo_nome = input(f"Nome atual [{produto['nome']}]: ").strip()
    novo_preco = input(f"Preço atual [{mostrar_dinheiro(produto['preco'])}]: ").strip()
    novo_estoque = input(f"Estoque atual [{produto['estoque']}]: ").strip()
    
    # Só muda o que o usuário preencheu
    if novo_nome != "":
        produto['nome'] = novo_nome
    
    if novo_preco != "":
        try:
            produto['preco'] = float(novo_preco)
        except:
            print("Preço inválido, mantendo o anterior...")
    
    if novo_estoque != "":
        try:
            produto['estoque'] = int(novo_estoque)
        except:
            print("Estoque inválido, mantendo o anterior...")
    
    print("\nProduto atualizado com sucesso!")
    input("Pressione Enter para continuar...")

def remover_produto():
    """Apaga um produto do sistema"""
    print("\n" + "="*50)
    print("           REMOVER PRODUTO")
    print("="*50)
    
    if len(produtos) == 0:
        print("Não tem nenhum produto cadastrado!")
        input("Pressione Enter para voltar...")
        return
    
    mostrar_produtos()
    
    codigo = input("\nDigite o código do produto para remover: ").strip()
    
    if codigo not in produtos:
        print("Produto não encontrado!")
        input("Pressione Enter para continuar...")
        return
    
    # Pede confirmação antes de apagar
    produto = produtos[codigo]
    confirmar = input(f"Tem certeza que quer remover '{produto['nome']}'? (S/N): ").upper()
    
    if confirmar == "S":
        # Remove o produto do dicionário
        del produtos[codigo]
        print(f"Produto '{produto['nome']}' removido!")
    else:
        print("Operação cancelada.")
    
    input("Pressione Enter para continuar...")

def mostrar_produtos():
    """Mostra todos os produtos cadastrados"""
    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        return
    
    print("\nLISTA DE PRODUTOS:")
    print("-" * 60)
    # Cabeçalho da tabela
    print(f"{'Código':<8} {'Nome':<20} {'Preço':<12} {'Estoque':<10}")
    print("-" * 60)
    
    # Mostra cada produto
    for codigo in produtos:
        p = produtos[codigo]  # 'p' é o dicionário do produto
        print(f"{codigo:<8} {p['nome']:<20} {mostrar_dinheiro(p['preco']):<12} {p['estoque']:<10}")
    
    print("-" * 60)

# ============================================
# 2. FUNÇÃO PARA REALIZAR VENDA
# ============================================

def realizar_venda():
    """Faz todo o processo de venda"""
    print("\n" + "="*50)
    print("           REALIZAR VENDA")
    print("="*50)
    
    # Verifica se tem produtos cadastrados
    if len(produtos) == 0:
        print("Cadastre produtos primeiro!")
        input("Pressione Enter para continuar...")
        return
    
    # Mostra os produtos disponíveis
    mostrar_produtos()
    
    # Cria o carrinho de compras (uma lista vazia)
    carrinho = []
    
    print("\n--- ADICIONE PRODUTOS AO CARRINHO ---")
    print("Digite 'FIM' no código para terminar a venda")
    
    # Loop para adicionar produtos
    while True:
        codigo = input("\nCódigo do produto (ou FIM): ").strip().upper()
        
        # Se digitar FIM, sai do loop
        if codigo == "FIM":
            break
        
        # Verifica se o produto existe
        if codigo not in produtos:
            print("Produto não encontrado! Tente outro código.")
            continue
        
        # Pega os dados do produto
        produto = produtos[codigo]
        
        # Mostra quanto tem no estoque
        print(f"Produto: {produto['nome']}")
        print(f"Estoque disponível: {produto['estoque']}")
        
        # Pede a quantidade
        quantidade = pedir_inteiro("Quantidade desejada: ")
        
        # VERIFICAÇÃO DO ESTOQUE (condicional importante!)
        if quantidade > produto['estoque']:
            print(f"ESTOQUE INSUFICIENTE! Temos apenas {produto['estoque']} unidades.")
            continue  # Volta para o início do loop
        
        # Calcula o subtotal (preço x quantidade)
        subtotal = produto['preco'] * quantidade
        
        # Cria um item para o carrinho
        item = {
            "codigo": codigo,
            "nome": produto['nome'],
            "preco_unitario": produto['preco'],
            "quantidade": quantidade,
            "subtotal": subtotal
        }
        
        # Adiciona o item na lista do carrinho
        carrinho.append(item)
        
        print(f"✓ Adicionado: {quantidade}x {produto['nome']}")
        print(f"  Subtotal: {mostrar_dinheiro(subtotal)}")
    
    # Verifica se o carrinho está vazio
    if len(carrinho) == 0:
        print("\nCarrinho vazio. Venda cancelada.")
        input("Pressione Enter para continuar...")
        return
    
    # Mostra o resumo da compra
    print("\n" + "="*50)
    print("           RESUMO DA COMPRA")
    print("="*50)
    
    # Calcula o total somando os subtotais
    total = 0
    for item in carrinho:
        print(f"{item['quantidade']}x {item['nome']} = {mostrar_dinheiro(item['subtotal'])}")
        total = total + item['subtotal']
    
    print("-" * 50)
    print(f"Subtotal: {mostrar_dinheiro(total)}")
    
    # APLICAÇÃO DE DESCONTO (condicional importante!)
    desconto = 0
    if total > 100:
        # 10% de desconto para compras acima de R$ 100
        desconto = total * 0.10
        total_final = total - desconto
        print(f"DESCONTO DE 10%: -{mostrar_dinheiro(desconto)}")
        print(f"TOTAL COM DESCONTO: {mostrar_dinheiro(total_final)}")
    else:
        total_final = total
        print(f"TOTAL: {mostrar_dinheiro(total_final)}")
    
    # Pergunta se confirma a venda
    confirmar = input("\nConfirmar venda? (S/N): ").upper()
    
    if confirmar != "S":
        print("Venda cancelada.")
        input("Pressione Enter para continuar...")
        return
    
    # ATUALIZA O ESTOQUE (loop para cada item)
    for item in carrinho:
        codigo_produto = item['codigo']
        quantidade_vendida = item['quantidade']
        
        # Diminui o estoque do produto
        produtos[codigo_produto]['estoque'] = produtos[codigo_produto]['estoque'] - quantidade_vendida
    
    # Salva a venda no histórico
    venda = {
        "data_hora": datetime.now(),  # Pega a data e hora atual
        "itens": carrinho,
        "total": total_final,
        "desconto": desconto
    }
    historico_vendas.append(venda)
    
    print("\n✓ VENDA REALIZADA COM SUCESSO!")
    
    # Gera o cupom fiscal
    gerar_cupom(venda)
    
    input("\nPressione Enter para continuar...")

# ============================================
# 3. FUNÇÃO PARA GERAR O CUPOM FISCAL
# ============================================

def gerar_cupom(venda):
    """Cria e mostra o cupom fiscal da venda"""
    print("\n" + "="*50)
    print("           CUPOM FISCAL")
    print("="*50)
    
    # Pega e formata a data/hora
    data = venda['data_hora'].strftime("%d/%m/%Y")
    hora = venda['data_hora'].strftime("%H:%M:%S")
    
    print(f"Data: {data}  Hora: {hora}")
    print("-" * 50)
    
    # Cabeçalho dos itens
    print(f"{'Qtd':<5} {'Produto':<25} {'Valor':>15}")
    print("-" * 50)
    
    # Mostra cada item
    for item in venda['itens']:
        nome = item['nome']
        qtd = item['quantidade']
        subtotal = item['subtotal']
        print(f"{qtd:<5} {nome:<25} {mostrar_dinheiro(subtotal):>15}")
    
    print("-" * 50)
    
    # Mostra o desconto se tiver
    if venda['desconto'] > 0:
        # Calcula o total sem desconto
        total_sem_desconto = 0
        for item in venda['itens']:
            total_sem_desconto = total_sem_desconto + item['subtotal']
        
        print(f"{'Subtotal:':<30} {mostrar_dinheiro(total_sem_desconto):>15}")
        print(f"{'Desconto (10%):':<30} {mostrar_dinheiro(venda['desconto']):>15}")
    
    # Mostra o total final
    print(f"{'TOTAL:':<30} {mostrar_dinheiro(venda['total']):>15}")
    
    print("="*50)
    print("     OBRIGADO PELA PREFERÊNCIA!")
    print("        VOLTE SEMPRE! 😊")
    print("="*50)

# ============================================
# 4. FUNÇÕES DE RELATÓRIOS
# ============================================

def ver_estoque_baixo():
    """Mostra produtos que estão acabando (menos de 5 unidades)"""
    print("\n" + "="*50)
    print("     PRODUTOS COM ESTOQUE BAIXO")
    print("         (menos de 5 unidades)")
    print("="*50)
    
    # Lista para guardar os produtos com estoque baixo
    produtos_baixo = []
    
    # Verifica cada produto
    for codigo in produtos:
        p = produtos[codigo]
        # SE o estoque for menor que 5 (condicional importante!)
        if p['estoque'] < 5:
            produtos_baixo.append(codigo)
    
    # Verifica se encontrou algum
    if len(produtos_baixo) == 0:
        print("\nÓtimo! Nenhum produto com estoque baixo!")
    else:
        print("\nATENÇÃO! Estes produtos precisam ser repostos:")
        print("-" * 50)
        
        for codigo in produtos_baixo:
            p = produtos[codigo]
            print(f"Código: {codigo}")
            print(f"Produto: {p['nome']}")
            print(f"Estoque atual: {p['estoque']} unidades")
            print("-" * 30)
        
        print(f"Total: {len(produtos_baixo)} produto(s) com estoque baixo")
    
    input("\nPressione Enter para continuar...")

def ver_vendas_do_dia():
    """Mostra todas as vendas de hoje"""
    print("\n" + "="*50)
    print("        VENDAS REALIZADAS HOJE")
    print("="*50)
    
    # Pega a data de hoje
    hoje = datetime.now().date()
    
    # Filtra só as vendas de hoje
    vendas_hoje = []
    for venda in historico_vendas:
        # Compara a data da venda com a data de hoje
        if venda['data_hora'].date() == hoje:
            vendas_hoje.append(venda)
    
    # Verifica se teve venda hoje
    if len(vendas_hoje) == 0:
        print("\nNenhuma venda realizada hoje ainda.")
    else:
        total_do_dia = 0
        
        # Mostra cada venda
        for numero in range(len(vendas_hoje)):
            venda = vendas_hoje[numero]
            hora = venda['data_hora'].strftime("%H:%M")
            
            print(f"\nVenda {numero + 1} - Horário: {hora}")
            
            # Conta quantos itens foram vendidos
            total_itens = 0
            for item in venda['itens']:
                total_itens = total_itens + item['quantidade']
            
            print(f"Itens vendidos: {total_itens}")
            print(f"Valor total: {mostrar_dinheiro(venda['total'])}")
            total_do_dia = total_do_dia + venda['total']
        
        # Mostra o resumo do dia
        print("\n" + "="*50)
        print(f"Total de vendas hoje: {len(vendas_hoje)}")
        print(f"Faturamento do dia: {mostrar_dinheiro(total_do_dia)}")
    
    input("\nPressione Enter para continuar...")

# ============================================
# 5. MENU PRINCIPAL DO SISTEMA
# ============================================

def menu():
    """Menu principal - o coração do sistema"""
    
    # Loop infinito (só sai quando o usuário escolher sair)
    while True:
        # Mostra o menu
        print("\n" + "="*50)
        print("        MERCADINHO DO BAIRRO")
        print("     Sistema de Gerenciamento")
        print("="*50)
        print("\nMENU PRINCIPAL:")
        print("1 - Cadastrar Produto")
        print("2 - Ver Produtos")
        print("3 - Editar Produto")
        print("4 - Remover Produto")
        print("5 - Realizar Venda")
        print("6 - Ver Estoque Baixo")
        print("7 - Ver Vendas do Dia")
        print("8 - Sair do Sistema")
        print("="*50)
        
        # Pede a opção do usuário
        opcao = input("\nEscolha uma opção (1-8): ").strip()
        
        # Verifica qual opção foi escolhida
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("\n" + "="*50)
            print("           PRODUTOS CADASTRADOS")
            print("="*50)
            mostrar_produtos()
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            realizar_venda()
        elif opcao == "6":
            ver_estoque_baixo()
        elif opcao == "7":
            ver_vendas_do_dia()
        elif opcao == "8":
            print("\nObrigado por usar o sistema!")
            print("Volte sempre! 👋")
            break  # Sai do loop while
        else:
            print("\nOpção inválida! Digite um número de 1 a 8.")
            input("Pressione Enter para continuar...")

# ============================================
# DADOS DE EXEMPLO PARA TESTAR
# ============================================

def colocar_produtos_exemplo():
    """Adiciona alguns produtos para você já começar testando"""
    # Criando produtos de exemplo
    produtos["001"] = {"nome": "Arroz 5kg", "preco": 22.90, "estoque": 3}
    produtos["002"] = {"nome": "Feijão 1kg", "preco": 8.50, "estoque": 8}
    produtos["003"] = {"nome": "Óleo de Soja", "preco": 7.99, "estoque": 2}
    produtos["004"] = {"nome": "Leite Integral", "preco": 4.50, "estoque": 12}
    produtos["005"] = {"nome": "Café 500g", "preco": 15.90, "estoque": 1}
    produtos["006"] = {"nome": "Açúcar 2kg", "preco": 6.99, "estoque": 6}
    
    print("Produtos de exemplo carregados! 🎉")

# ============================================
# INÍCIO DO PROGRAMA
# ============================================

# Esta é a parte que realmente executa quando rodamos o programa
print("Iniciando o sistema...")
print("Carregando produtos de exemplo...")
colocar_produtos_exemplo()

# Inicia o menu principal
menu()