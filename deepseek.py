produtos = {}  # chave: código (string), valor: dict com nome, preco, estoque

def cadastrar_produtos():
    codigo = input("Digite o código: ")
    if codigo in produtos:
        print("Código já existe!")
        return
    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço: R$ "))
    estoque = int(input("Digite o estoque: "))
    produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque}
    print(f"Produto {nome} cadastrado com sucesso!")

def compra():
    carrinho = []
    total = 0.0
    while True:
        codigo = input("Digite o código (ou '000' para finalizar): ")
        if codigo == '000':
            break
        if codigo not in produtos:
            print("Produto não cadastrado!")
            continue
        qtd = int(input("Quantidade: "))
        if qtd > produtos[codigo]['estoque']:
            print("Estoque insuficiente!")
            continue
        # calcula subtotal
        subtotal = produtos[codigo]['preco'] * qtd
        total += subtotal
        # atualiza estoque
        produtos[codigo]['estoque'] -= qtd
        carrinho.append({'codigo': codigo, 'qtd': qtd, 'subtotal': subtotal})
        print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Total da compra: R$ {total:.2f}")
    return carrinho, total

compra()