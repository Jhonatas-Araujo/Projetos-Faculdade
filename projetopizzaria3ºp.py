produtos = (
    {'id': 1, 'sabor': 'Calabresa', 'preco': 35.00, 'receita': 'Molho de tomate, muçarela, calabresa, cebola e óregano'},
    {'id': 2, 'sabor': 'Quatro queijos', 'preco': 40.00, 'receita': 'Molho de tomate, Muçarela, Provolone, Parmesão, Gorgonzola e  orégano.'},
    {'id': 3, 'sabor': 'Portuguesa', 'preco': 35.00, 'receita': 'Molho de tomate, Muçarela, Presunto, Ovos, Cebola, Azeitona e  orégano.'},
    {'id': 4, 'sabor': 'Frango com catupiry', 'preco': 38.00, 'receita': 'Molho de tomate, Muçarela, Frango, Cebola, Catupiry, Azeitona e  orégano.'},
    {'id': 5, 'sabor': 'Bacon', 'preco': 40.00, 'receita': 'Molho de tomate, Muçarela, Bacon, Milho e orégano.'},
    {'id': 6, 'sabor': 'Carne de Sol', 'preco': 45.00, 'receita': 'Molho de tomate, Muçarela, Carne Seca Desfiada, Cebola, Pimentãoe  orégano.'},
    {'id': 7, 'sabor': 'Hot-Dog', 'preco': 40.00, 'receita': 'Molho de tomate, Muçarela, Salsicha, Batata Palha e orégano.'},
    {'id': 8, 'sabor': 'Chocolate c/morangos', 'preco': 45.00, 'receita': 'Chocolate derretido, Morangos, e Granulado de chocolate.'},
    {'id': 9, 'sabor': 'Pepperoni', 'preco': 40.00, 'receita': 'Molho de tomate, Muçarela, Pepperoni, e orégano.'}
)

carrinho = []
temp = []

def exibirOpcoes():
    print('\n\n')
    print('1 - Observar o cardápio')
    print('2 - Exibir produtos no carrinho')
    print('3 - Limpar Carrinho de compras')
    print('4 - Sair')

def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Sabor: {1} - Preço: ${2} \nReceita: {3} \n'.format(p['id'], p['sabor'], p['preco'], p['receita']))


opcao = '1'

def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['sabor']

while opcao != '4':
    exibirOpcoes()
    opcao = input('Digite a opção: ')
    if opcao < '1' or opcao > '4':
        print('\n')
        print("Opção escolhida inválida!")
        print('Encerrando sistema...')
        break
    if opcao == '1':
        print('\n\n')
        exibirProdutos()
        print("Id: 10 - Para sair do sistema")
        print()
        id = int(input('Digite o identificador do produto: '))
        if id == 10:
            print('\n')
            print("Encerrando sistema...")
            break
        if id < 1 or id > 10:
            print('\n')
            print('ID do produto não indentificado!')
            print("Encerrando sistema...")
            break      
        quantidade = int(input('Digite a quantidade: '))
        if quantidade < 1:
            print('Esta quantidade não é aceita!')
            print("Encerrando sistema...")
            break
        else:
            print('\n')
            print("O pedido foi adicionado ao carrinho!")  
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
        print('Preço total: ${0}'.format(somatorio))
    if opcao == '3':
        carrinho = []
        print('\n')
        print("Seu carrinho foi limpo!")
    if opcao == '4':
        print('\n')
        print('Volte Sempre!')
        break