menu = """  
        [s] - SAQUE                                                  
        [d] - DEPÓSITO                                               
        [e] - EXTRATO                                                
        [l] - SAIR                                                                               
    """
# Acima, contém a variável contendo a menssagem inicial 

saque = 0 # Variável para saque
depositar = 0 # Variável para depósito 
opcao = "" # Variável para a escolhas das opcões do MENU
saldo = 0 # Variável para saldo
limite_saque = 0 # Limite de saque é 3, o limite de saque é R$ 500,00
VALOR_LIMITE_DE_SAQUE = float(500)
extrato_saque = "" # Variável para receber os saques 
extrato_deposito = "" # Variável para receber os depósitos

while True: # Estrutura de repetição while = True. Com o objetivo de ficar sempre em Loop3
    print(menu)
    opcao = input("") # Exibindo a mensagem do menu e pegando a opção pelo input, atribuindo na variável opcao

    if opcao == "s": # Condição para a opção de saque
        saque = float(input("Informe o saque: R$ ")) # Após a checagem, pede o informe do saque

        if saque >= 0: 
            if saque <= VALOR_LIMITE_DE_SAQUE and saldo >= saque and limite_saque != 3: # Condição para verificar se o limite de saque foi atingido, tem que ser diferente de 3: #Verificando se o valor do saque é até 500 e o saldo da conta tem que ser maior > saque
                print("Saque realizado!")
                saldo -= saque # Após a confirmação da condição, iremos fazer a subtração do saldo com o saque
                limite_saque += 1 # Contador de limite de saques diários
                extrato_saque += f"Saque: - R$ {saque:.2f}\n"
                
            elif saldo < saque: # Condicional para caso o usuario tente sacar um dinheiro que não tenha
                print (f"Saldo indisponível para saque!") # print da mensagem e com o valor do saque. Irei adiocionar +

            elif saque > VALOR_LIMITE_DE_SAQUE: # Condicional para caso ele ultrapasse o valor limite de saque
                    print(f"Ops, o limite de saque é R${VALOR_LIMITE_DE_SAQUE: .2f}") 
            else:
                print(f" Quantidade de saques diários atingido = {limite_saque}")     

        else:
            print(f"Error, você está tentando sacar valores negativos!") # Caso ele atinga o limite de saque diário


    elif opcao == "d": # Condição para a opção de depósito que é 1 
        depositar = float(input("Informe o depósito: R$ ")) # Atribuindo o valor de depósito na variável depositar

        if depositar > 0: # Condição para o depósito ser um número maior que 0
            print("Depósito realizado!")
            saldo += depositar #Atribuindo o depósito no saldo, após a confirmação que o valor do depósito é maior que zero e não menor
            #print(saldo)
            extrato_deposito += f"Depósito: + R$ {depositar:.2f}\n"
            # Acima, estou atribuindo a variável extrato com o saldo e o ultmo valor que depositei

        else: # Condição para caso o cliente digite valores negativos para depósito
            print("Você digitou valores negativos, tente novamente")
   
    elif opcao == "e":
        
        extrato =  f"""
------------ EXTRATO -----------
SALDO = R$ {saldo:.2f}

{extrato_saque}
--------------------------------
{extrato_deposito} 
--------------------------------    
            """
        print(extrato)

    elif opcao == "l": # Essa condição checa se a opção 3 foi escolhida e encerrar o loop com break   
        print("Saindo do sistema...") # Mensagem de logout do sistema
        break # Cortando o loop com o break
    
    else: 
        print("Opção invalida, tente novamente")
    

