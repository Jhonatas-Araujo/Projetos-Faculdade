produtos = (
    {'id': 1, 'sabor': 'Calabresa', 'preco': 35, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'},
    {'id': 2, 'sabor': 'Quatro queijos', 'preco': 35, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'},
    {'id': 3, 'sabor': 'Portuguesa', 'preco': 36, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'},
    {'id': 4, 'sabor': 'Frango com catupiry', 'preco': 38, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'},
    {'id': 5, 'sabor': 'Bacon', 'preco': 40, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'},
    {'id': 6, 'sabor': 'Carne de Sol', 'preco': 45, 'receita': 'Molho de tomatem, mussarela, calabresa, cebola e óregano'}
)

carrinho = []
temp = []

def exibirOpcoes():
    print('\n\n')
    print('1 - Observar o cardápio')
    print('2 - Exibir produtos no carrinho e o valor total')
    print('3 - Limpar Carrinho de compras')
    print('4 - Sair')

def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Sabor: {1} - Preço: {2} - Receita:{3} \n'.format(p['id'], p['sabor'], p['preco'], p['receita']))


opcao = '1'

def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['sabor']

while opcao != '4':
    exibirOpcoes()
    opcao = input('Digite a opção: ')
    if opcao < '1' or opcao > '4':
        print("Opção escolhida inválida!")
        print('Encerrando sistema...')
        break
    if opcao == '1':
        print('\n\n')
        exibirProdutos()
        print("Id: 7 - Para sair do sistema")
        print()
        id = int(input('Digite o identificador do produto: '))
        if id == 7:
            print("Encerrando sistema...")
            break
        if id < 1 or id > 7:
            print('ID do produto não indentificado!')
            break      
        quantidade = int(input('Digite a quantidade: '))
        if quantidade < 1:
            print('Valores negativos não são aceitos!')
            break
        carrinho.append({'id': id, 'quantidade': quantidade})
    if opcao == '2':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                        (produto['preco'] * item['quantidade'])
                    break

            print(
                'Sabor: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))
    if opcao == '3':
        carrinho = []
    if opcao == '4':
        print('Volte Sempre!')