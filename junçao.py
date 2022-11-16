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