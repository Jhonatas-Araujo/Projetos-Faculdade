cadastros = []
valorPassagem=0
valorPassagem2=0
valorPassagem3=0
valorPassagem4=0
valorPassagem5=0   
valorTotal=0
editare = 0
qtdpassTotal = 0
cpf = 0
opcao = 0

langue = int(input('''


░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░  ░█████╗░███████╗██████╗░███████╗░█████╗░
██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║  ███████║█████╗░░██████╔╝█████╗░░██║░░██║
░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░██║░░██║
██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║  ██║░░██║███████╗██║░░██║███████╗╚█████╔╝
╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░

▐░░░░░░░░ ESCOLHA A LINGUAGEM ░░░░░░░░▌

Português -> [1]
English -> [0]
'''))
if langue == 1:
        def  cadastrar():
            print('Antes de avançarmos com a compra faça seu cadastro de usuário:')
            nome = input("Digite seu nome: ")
            cpf = int(input("Digite seu cpf: "))

            if cpf <= 100000000000: 
                datanasc = input("Data de nascimento (DD/MM/AAAA): ")
                tell = int(input("Digite seu telefone para contato(+55): "))
                if tell <= 100000000000:
                    email = input("Digite seu e-mail para contato: ")
                    print('Seu cadastro será enviado para análise, verifique se todas informações estão corretas.')
                    cadastro = {"nome": nome, "cpf": cpf,"datanasc":datanasc,"telefone":tell,"email":email,"quant":qtdpassTotal}
                    cadastros.append(cadastro)
                    for valor in cadastros:
                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO REGISTRADO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                        print(f"Nome:{valor['nome']}")
                        print(f"CPF:{valor['cpf']}")
                        print(f"Data de nascimento:{valor['datanasc']}")
                        print(f"Telefone:{valor['telefone']}")
                        print(f"E-mail:{valor['email']}\n")
                        editare = int(input("CADASTRO CORRETO? Se dedeja editar digite [1], se não digite [0]: \n"))
                        if editare == 1:   
                            print("          ▐░░░░░░░░ EDITAR CADASTRO ░░░░░░░░\n")
                            print("DESEJA EDITAR NOME? DIGITE [1]")
                            print("DESEJA EDITAR CPF? DIGITE [2]")
                            print("DESEJA EDITAR DATA? DIGITE [3]")
                            print("DESEJA EDITAR TELL? DIGITE [4]")
                            print("DESEJA EDITAR EMAIL? DIGITE [5]\n")
                            editarem = int(input("Digite um número: "))
                            if editarem == 1:
                                    cadastro['nome'] = input("Digite o novo nome: ")
                            elif editarem == 2:
                                    cadastro['cpf'] = input("Digite o novo CPF: ")
                            elif editarem == 3:
                                    cadastro['datanasc'] = input("Digite a nova data: ")
                            elif editarem == 4:
                                    cadastro['telefone'] = input("Digite o novo telefone: ")
                            elif editarem == 5:
                                    cadastro['cpf'] = input("Digite o novo Email: ")         
                        else:
                            return
                else:
                    print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ INSIRA UM TELEFONE VÁLIDO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
                    cadastrar()
            else:        
                print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ INSIRA UM CPF VÁLIDO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
                cadastrar()  

        while True:
            
            
            print('''\n        ▂▃▄▅▆▇█▓▒░ SISTEMA AÉREO DE SÃO LUÍS ░▒▓█▇▆▅▄▃▂ 

            ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Menu de Opções ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
                ''')
            
            opcao = int(input('''
                1 - COMPRAR PASSAGEM
                2 - CONSULTAR CADASTRO
                3 - LOCALIZAR CADASTRO
                4 - SAIR DO SISTEMA 
                
            ESCOLHA UM NUMERO DE 1 A 4: ''' ))
            
            if opcao < 0 or opcao >= 5:
                print("Escolha inválida! Sistema encerrado...")
                break
            if opcao == 1:
                    print("\n    ▐░░░░░░░░ CADASTRO DO USUÁRIO ░░░░░░░░▌\n")
                    cadastrar()
            
                    print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Bem-vindo ao sistema de compras de passagens aéreas de São Luís ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n''')
                        
                    destinos=["Rio Janeiro","São Paulo","Fortaleza","Brasília","Santa Catarina\n"]
                    for rota,destinosdisponiveis in enumerate(destinos):
                        print("%s %s" % (rota+1,destinosdisponiveis))
                            
                    assentosLivres=[30,30,30,30,30]
                    quantidadeRotas=len(assentosLivres)

                    for rota,assentosVagos in enumerate (assentosLivres):
                        print('Rota %d possui %d assentos livres' % (rota+1,assentosVagos))
                    while True:
                        qtdtotalpass = 0   
                        rotaEscolhida=int(input("Escolha uma rota de 1 a %d (Para finalizar a compra digite 0): " % quantidadeRotas ))
                        if rotaEscolhida == 0:
                            print("Sistema encerrado!")
                            break
                        if rotaEscolhida > quantidadeRotas or rotaEscolhida<0:
                            print("Rota inválida...")
                            break
                        elif assentosLivres[rotaEscolhida-1] == 0:
                            print('''\n Não temos mais vagas para essa rota.
            Escolha outra rota...\n''')
                        else:
                            quantidadePassagens=int(input("Quantas passagens deseja comprar? "))
                            if quantidadePassagens > assentosLivres[rotaEscolhida-1]:
                                print("Quantidade de passagens superior às disponíveis")
                            elif quantidadePassagens < 1:
                                print("Escolha uma quantidade de passagens maior que 0")
                            else:
                                print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Bem-vindo ao sistema de compras de passagens aéreas de São Luís ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n''')
                                for rota,destinosdisponiveis in enumerate(destinos):
                                    print("%s %s" % (rota+1,destinosdisponiveis))  
                                assentosLivres[rotaEscolhida-1] -= quantidadePassagens
                                for rota,assentosVagos in enumerate (assentosLivres):
                                    print('Rota %d possui %d assentos livres' % (rota+1,assentosVagos))
                                
                                qtdtotalpass = quantidadePassagens+qtdtotalpass 
                                if rotaEscolhida == 1:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem = quantidadePassagens*500
                                    valorTotal = valorPassagem+valorTotal
                                    print("O valor de $%d foi adicionado ao seu carrinho. O valor total da compra é R$%d " % (valorPassagem,valorTotal))
                                if rotaEscolhida == 2:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem2 = quantidadePassagens*650
                                    valorTotal = valorPassagem2+valorTotal
                                    print("O valor a ser pago é $%d foi adicionado ao seu carrinho. O valor total da compra é R$%d " % (valorPassagem2,valorTotal))
                                if rotaEscolhida == 3:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem3 = quantidadePassagens*850
                                    valorTotal = valorPassagem3+valorTotal
                                    print("O valor a ser pago é $%d foi adicionado ao seu carrinho. O valor total da compra é R$%d " % (valorPassagem3,valorTotal))
                                if rotaEscolhida == 4:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem4 = quantidadePassagens*1000
                                    valorTotal = valorPassagem4+valorTotal
                                    print("O valor a ser pago é $%d foi adicionado ao seu carrinho. O valor total da compra é R$%d " % (valorPassagem4,valorTotal))
                                if rotaEscolhida == 5:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem5 = quantidadePassagens*700
                                    valorTotal = valorPassagem5+valorTotal
                                    print("O valor a ser pago é $%d foi adicionado ao seu carrinho. O valor total da compra é $%d" % (valorPassagem5,valorTotal))

            

            if opcao == 4:
                    print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ VOLTE SEMPRE  ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎


                              ████████
          ██████           ███▒▒▒▒▒▒▒▒███
         █▒▒▒▒▒▒█       ███▒▒▒▒▒▒▒▒▒▒▒▒▒███
          █▒▒▒▒▒▒█    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
           █▒▒▒▒▒█   ██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
            █▒▒▒█   █▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
          █████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
          █▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
        ██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
       ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
       ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
        █▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
         ██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
          ████████████   █████████████████

                    \n''')
                    break
                                
            if opcao == 2:
                                if len(cadastros) > 0:
                                    for valor in cadastros:
                                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTROS REGISTRADOS ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                        print(f"Nome:{valor['nome']}")
                                        print(f"CPF:{valor['cpf']}")
                                        print(f"Data de nascimento:{valor['datanasc']}")
                                        print(f"Telefone:{valor['telefone']}")
                                        print(f"E-mail:{valor['email']}")
                                        print(f"Passagens: %d" % (qtdpassTotal))
                                        
                                        print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                else:
                                    print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ NENHUM CADASTRO REGISTRADO NO SISTEMA ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                    
                                    
                                
                                        


            if opcao == 3:
                        pesquisa = input("Digite o nome: ")
                        pesquisa1 = int(input("Digite o CPF: "))

                        if len(cadastros) > 0:
                                for valor in cadastros:
                                    if valor["nome"] == pesquisa or valor["cpf"] == pesquisa1:
                                            print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO ENCONTRADO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")                
                                            print(f"Nome:{valor['nome']}")
                                            print(f"CPF:{valor['cpf']}")
                                            print(f"Data de nascimento:{valor['datanasc']}")
                                            print(f"Telefone:{valor['telefone']}")
                                            print(f"E-mail:{valor['email']}")
                                            print(f"Passagens: %d" % (qtdpassTotal))
                                            
                                            print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                    else:
                                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO NÃO ENCONTRADA! ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
elif langue == 0:
    def  cadastrar():
            print('Before proceeding with the purchase, make your user registration:')
            nome = input("Type your name: ")
            cpf = int(input("Enter your CPF: "))

            if cpf <= 100000000000: 
                datanasc = input("Date of birth (DD/MM/YYYY): ")
                tell = int(input("Enter your contact phone (+55): "))
                if tell <= 100000000000:
                    email = input("Enter your contact email: ")
                    print('Your registration will be sent for analysis, check that all information is correct.')
                    cadastro = {"nome": nome, "cpf": cpf,"datanasc":datanasc,"telefone":tell,"email":email,"quant":qtdpassTotal}
                    cadastros.append(cadastro)
                    for valor in cadastros:
                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ REGISTERED REGISTRATION ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                        print(f"Nome:{valor['nome']}")
                        print(f"CPF:{valor['cpf']}")
                        print(f"Data de nascimento:{valor['datanasc']}")
                        print(f"Telefone:{valor['telefone']}")
                        print(f"E-mail:{valor['email']}\n")
                        editare = int(input("CORRECT REGISTRATION? If you want to edit enter [1], if not enter [0]: \n"))
                        if editare == 1:   
                            print("          ▐░░░░░░░░ EDIT REGISTRATION ░░░░░░░░\n")
                            print("WANT TO EDIT NAME? TYPE [1]")
                            print("DO YOU WANT TO EDIT CPF? TYPE [2]")
                            print("WANT TO EDIT DATE? TYPE [3]")
                            print("WANT TO EDIT TELL? TYPE [4]")
                            print("WANT TO EDIT EMAIL? TYPE [5]\n")
                            editarem = int(input("Enter a number: "))
                            if editarem == 1:
                                    cadastro['nome'] = input("Enter the new name: ")
                            elif editarem == 2:
                                    cadastro['cpf'] = input("Enter the new CPF: ")
                            elif editarem == 3:
                                    cadastro['datanasc'] = input("Enter the new date: ")
                            elif editarem == 4:
                                    cadastro['telefone'] = input("Enter the new phone: ")
                            elif editarem == 5:
                                    cadastro['cpf'] = input("Enter the new Email: ")         
                        else:
                            return
                else:
                    print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ INSERT A VALID PHONE ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
                    cadastrar()
            else:        
                print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ ENTER A VALID CPF ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎")
                cadastrar()  

    while True:
            
            
            print('''\n        ▂▃▄▅▆▇█▓▒░ SÃO LUÍS AIR SYSTEM ░▒▓█▇▆▅▄▃▂ 

            ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Options menu ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
                ''')
            
            opcao = int(input('''
                1 - BUY TICKET
                2 - CONSULT REGISTRATION
                3 - LOCATE REGISTRATION
                4 - EXIT THE SYSTEM
                
            CHOOSE A NUMBER FROM 1 TO 4: ''' ))
            
            if opcao < 0 or opcao >= 5:
                print("Invalid choice! System closed...")
                break
            if opcao == 1:
                    print("\n    ▐░░░░░░░░ USER REGISTRATION ░░░░░░░░▌\n")
                    cadastrar()
            
                    print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ Welcome to the São Luís airline ticket purchase system ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n''')
                        
                    destinos=["Rio Janeiro","São Paulo","Fortaleza","Brasília","Santa Catarina\n"]
                    for rota,destinosdisponiveis in enumerate(destinos):
                        print("%s %s" % (rota+1,destinosdisponiveis))
                            
                    assentosLivres=[30,30,30,30,30]
                    quantidadeRotas=len(assentosLivres)

                    for rota,assentosVagos in enumerate (assentosLivres):
                        print('Rota %d possui %d assentos livres' % (rota+1,assentosVagos))
                    while True:
                        qtdtotalpass = 0   
                        rotaEscolhida=int(input("Choose a route from 1 to %d (To checkout, enter 0): " % quantidadeRotas ))
                        if rotaEscolhida == 0:
                            print("System closed!")
                            break
                        if rotaEscolhida > quantidadeRotas or rotaEscolhida<0:
                            print("invalid route...")
                            break
                        elif assentosLivres[rotaEscolhida-1] == 0:
                            print('''\n We have no more vacancies for this route.
            choose another route...\n''')
                        else:
                            quantidadePassagens=int(input("How many tickets do you want to buy?"))
                            if quantidadePassagens > assentosLivres[rotaEscolhida-1]:
                                print("More tickets than available")
                            elif quantidadePassagens < 1:
                                print("Choose a number of tickets greater than 0")
                            else:
                                print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎Welcome to the São Luís airline ticket purchase system∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n''')
                                for rota,destinosdisponiveis in enumerate(destinos):
                                    print("%s %s" % (rota+1,destinosdisponiveis))  
                                assentosLivres[rotaEscolhida-1] -= quantidadePassagens
                                for rota,assentosVagos in enumerate (assentosLivres):
                                    print('Route %d has %d free seats' % (rota+1,assentosVagos))
                                
                                qtdtotalpass = quantidadePassagens+qtdtotalpass 
                                if rotaEscolhida == 1:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem = quantidadePassagens*500
                                    valorTotal = valorPassagem+valorTotal
                                    print("The value of $%d has been added to your cart. The total purchase amount is R$%d " % (valorPassagem,valorTotal))
                                if rotaEscolhida == 2:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem2 = quantidadePassagens*650
                                    valorTotal = valorPassagem2+valorTotal
                                    print("The amount to be paid is $%d has been added to your cart. The total purchase amount is R$%d " % (valorPassagem2,valorTotal))
                                if rotaEscolhida == 3:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem3 = quantidadePassagens*850
                                    valorTotal = valorPassagem3+valorTotal
                                    print("The amount to be paid is $%d has been added to your cart. The total purchase amount is R$%d" % (valorPassagem3,valorTotal))
                                if rotaEscolhida == 4:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem4 = quantidadePassagens*1000
                                    valorTotal = valorPassagem4+valorTotal
                                    print("The amount to be paid is $%d has been added to your cart. The total purchase amount is R$%d " % (valorPassagem4,valorTotal))
                                if rotaEscolhida == 5:
                                    qtdpassTotal = quantidadePassagens+qtdpassTotal
                                    valorPassagem5 = quantidadePassagens*700
                                    valorTotal = valorPassagem5+valorTotal
                                    print("The amount to be paid is $%d has been added to your cart. The total purchase amount is $%d" % (valorPassagem5,valorTotal))

            

            if opcao == 4:
                    print('''\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CHECK BACK OFTEN ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎


                              ████████
          ██████           ███▒▒▒▒▒▒▒▒███
         █▒▒▒▒▒▒█       ███▒▒▒▒▒▒▒▒▒▒▒▒▒███
          █▒▒▒▒▒▒█    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
           █▒▒▒▒▒█   ██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
            █▒▒▒█   █▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
          █████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
          █▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
        ██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
       ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
       ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
        █▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
         ██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
          ████████████   █████████████████

                    \n''')
                    break
                                
            if opcao == 2:
                                if len(cadastros) > 0:
                                    for valor in cadastros:
                                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ REGISTERED REGISTRATIONS ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                        print(f"Nome:{valor['nome']}")
                                        print(f"CPF:{valor['cpf']}")
                                        print(f"Data de nascimento:{valor['datanasc']}")
                                        print(f"Telefone:{valor['telefone']}")
                                        print(f"E-mail:{valor['email']}")
                                        print(f"Passagens: %d" % (qtdpassTotal))
                                        
                                        print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                else:
                                    print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ NO REGISTRATION REGISTERED IN THE SYSTEM ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                    
                                    
                                
                                        


            if opcao == 3:
                        pesquisa = input("Digite o nome: ")
                        pesquisa1 = int(input("Digite o CPF: "))

                        if len(cadastros) > 0:
                                for valor in cadastros:
                                    if valor["nome"] == pesquisa or valor["cpf"] == pesquisa1:
                                            print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO ENCONTRADO ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")                
                                            print(f"Nome:{valor['nome']}")
                                            print(f"CPF:{valor['cpf']}")
                                            print(f"Data de nascimento:{valor['datanasc']}")
                                            print(f"Telefone:{valor['telefone']}")
                                            print(f"E-mail:{valor['email']}")
                                            print(f"Passagens: %d" % (qtdpassTotal))
                                            
                                            print("∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")
                                    else:
                                        print("\n∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎ CADASTRO NÃO ENCONTRADA! ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎\n")