import getpass

def cadastro_login():

    print(f'''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Bem vindo ao cadastro do cliente ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ 

         ~ Preencha os campos abaixo para realizar o cadastro 🙂
''')

    nome = str(input("- Digite seu nome completo: "))
    cpf = input("- Digite seu CPF: ") 
    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    datanasc = input("- Digite o dia de nascimento (01 a 31): ") ,input("- Digite o mês de nascimento (01 a 12): ") ,input("- Digite o ano de nascimento: ")
    email = (input("- Digite seu email: "))
    telefone = (input("- Digite seu telefone de contato: "))
    senha = getpass.getpass("- Digite uma senha para sua conta: ")

    print(f'''
         ~ Agora cadastre seu endereço 🙂
''')

    cep = int(input("Digite o CEP: "))
    bairro = (input("Digite o bairro: "))
    rua = (input("Digite a rua: "))
    numerolocal = int(input("Digite o numero da casa: "))
    comp = (input("Digite um complemento (CASA/CONDOMÍNIO): "))

    print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO REGISTRADO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
    print(f"Nome:",nome)
    print(f"CPF:",cpf)
    print(f"Data de nascimento:",datanasc)
    print(f"Telefone:",telefone,)
    print(f"E-mail:",email,)
    print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ ENDEREÇO PARA ENTREGA ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
    print(f"CEP:",cep)
    print(f"Bairro:",bairro)
    print(f"Rua:",rua)
    print(f"Número:",numerolocal)
    print(f"Complemento:",comp)

    editare = int(input("\nENDEREÇO CORRETO? Se dedeja editar digite [1], se não digite [0]: \n"))

    if editare == 1:   
        print("            ▐░░░░░░░░ EDITAR ENDEREÇO ░░░░░░░░\n")
        print("DESEJA EDITAR CEP?    DIGITE  [1]")
        print("DESEJA EDITAR BARRO?  DIGITE  [2]")
        print("DESEJA EDITAR RUA?    DIGITE  [3]")
        print("DESEJA EDITAR NÚMERO? DIGITE  [4]")
        print("DESEJA EDITAR COMP?   DIGITE  [5]")

        editarem = int(input("Digite um número: "))

        if editarem == 1:
            cep = input("Digite o novo CEP: ")
        elif editarem == 2:
            bairro = input("Digite o novo bairro: ")
        elif editarem == 3:
            rua = input("Digite a nova rua: ")    
        elif editarem == 4:
            numerolocal = input("Digite o novo número: ")
        elif editarem == 5:
            comp = input("Digite o novo complemento: ")
        
        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ ENDEREÇO REGISTRADO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
        print(f"CEP:",cep)
        print(f"Bairro:",bairro)
        print(f"Rua:",rua)
        print(f"Número:",numerolocal)
        print(f"Complemento:",comp)


    def login():
        print("                   ▐░░░░░░░░ LOGIN ░░░░░░░░")
        emaillogin = (input("\n- Digite seu email para login: "))
        senhallogin = (getpass.getpass("- Digite sua senha: "))

        if emaillogin == email and senhallogin == senha:
            print("\n          ▐░░░░░░░░ LOGIN EFETUADO COM SUCESSO ░░░░░░░░")
            print("\n+ Olá",nome,":). Vamos fazer seu pedido agora...\n")
        else:
            print("E-mail ou senha incorretos!")
            login()
    login()

cadastro_login()




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
        
        #sadasdasdasdas
        print('\n\n')
        print('''FORMAS DE PAGAMENTO

[ 1 ] Chave Aleatória (PIX)
[ 2 ] Cartão de Crédito/Débito
[ 3 ] Dinheiro
[ 4 ] Cancelar Pedido
''')


opção = int(input('Qual será a forma de pagamento?'))

print("")
if opção == 1:
    print('QRCODE')
    print("")
    print('Copiar!')
    print("\n")
    print("Pedido realizado com sucesso!")
    print('Agradeçemos pela preferência. Volte sempre!')

if opção == 2:
    print('''
[ 1 ] Crédito
[ 2 ] Débito)''')
    debitocredito = int(input('Débito ou Crédito?')) 
    
    nomecar = input('Nome Impresso no cartão:'),
    numerocar = input('Número do cartão:'),
    validadecar = input('Validade: '),
    cvccar = input('Código de Verificação:  '),
    nasccar = input('Data de nascimento: '),
    cpfcar = input('CPF do titular:')
    print("Pedido realizado com sucesso!")
    print('Agradeçemos pela preferência. Volte sempre!')
if opção == 3:
    print("O valor total da sua compra é de:R${0} ".format(somatorio))
    print('''
[ 1 ] Sim
[ 2 ] Não''')
    troco = int(input('Precisa de troco?'))
    if troco == 1:
        troco1 = input("Para quanto?")
        troco2 = troco1 - somatorio
        print("seu troco será de:", troco2)
        print("Pedido realizado com sucesso!")
        print('Agradeçemos pela preferência. Volte sempre!')

    if troco == 2:
        print("Pedido realizado com sucesso!")
        print('Agradeçemos pela preferência. Volte sempre!')


if opção == 4:
    print("Pedido Cancelado!")
    print("Volte Sempre!")
