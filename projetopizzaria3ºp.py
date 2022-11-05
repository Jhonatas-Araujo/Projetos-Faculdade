produtos = (
    {'id': 1, 'sabor': 'Calabresa', 'preco': 35},
    {'id': 2, 'sabor': 'Frango com catupiry', 'preco': 38},
    {'id': 3, 'sabor': 'Bacon', 'preco': 40},
    {'id': 4, 'sabor': 'Carne de Sol', 'preco': 45}
)

carrinho = []
temp = []

def exibirOpcoes():
    print('\n\n')
    print('1 - Observar o cardápio')
    print('2 - Remover pedido')
    print('3 - Exibir produtos e o valor total')
    print('4 - Limpar Carrinho de compras')
    print('5 - Sair')


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Sabor: {1} - Preço: {2}\n'.format(p['id'], p['sabor'], p['preco']))


opcao = '1'


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['sabor']


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao < '1' or opcao > '5':
        print("Opção escolhida inválida!")
        print('Sistema encerrando...')
        break
    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o identificador do produto: '))
        if id < 1 or id > 4:
            print('ID do produto não indentificado!')
            break
        quantidade = int(input('Digite a quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})
        temp.append({'id': id, 'quantidade': quantidade})
        
    if opcao == '2':
        id = int(input('Digite o identificador do produto: '))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                carrinho.append(item)

    if opcao == '3':
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

    if opcao == '4':
        carrinho = []
        temp = []
    if opcao == '5':
        print('Volte Sempre!')
        
