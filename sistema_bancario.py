menu = """  
        [s] - SAQUE                                                  
        [d] - DEPÓSITO                                               
        [e] - EXTRATO                                                
        [l] - SAIR
        [u] - CRIAR CONTA
        [m] - MOSTRAR CONTAS

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
nome = ""
data_nascimento = ""
cpf = 0
endereco = ""
usuarios = ""
lista_de_cpfs_cadastrados = []
numero_da_conta = 0
NUMERO_DA_AGENCIA = "0001"

class Cliente:
     
     def __init__(self, numero_da_conta, NUMERO_DA_AGENCIA, /, *, nome, data_nascimento, cpf, endereco, usuarios):
          self.numero_da_conta = numero_da_conta
          self.NUMERO_DA_AGENCIA = NUMERO_DA_AGENCIA
          self.nome = nome
          self.data_nascimento = data_nascimento
          self.cpf = cpf
          self.endereco = endereco
          self.usuarios = usuarios

     def criar_conta(self):
            self.nome = input("Digite seu nome: ")
            self.data_nascimento = input("Data nascimento: ")
            self.endereco = input("Endereço (Logradoro - bairro - cidade/sigla - estado ): ")

            self.usuarios += f"""
            ------------INFORMAÇÕES PESSOAIS--------------

            Nome: {self.nome.title()}
            Data de Nascimento: {self.data_nascimento}
            CPF: {self.cpf}
            Endereço: {self.endereco.upper()}

            ------------INFORMAÇÕES CONTA------------------
                    
            NÚMERO DA CONTA: {self.numero_da_conta}     
            AGÊNCIA: {self.NUMERO_DA_AGENCIA}

            -----------------------------------------------

            """
            return self.usuarios, self.cpf

class Deposito:
     
     def __init__(self, saldo, depositar, extrato_deposito, /):
          self.saldo = saldo
          self.depositar = depositar
          self.extrato_deposito = extrato_deposito

     def depositar_em_conta(self):
        if self.depositar > 0: # Condição para o depósito ser um número maior que 0
                print("Depósito realizado!")
                self.saldo += self.depositar #Atribuindo o depósito no saldo, após a confirmação que o valor do depósito é maior que zero e não menor
                #print(saldo)
                self.extrato_deposito += f"Depósito: + R$ {self.depositar:.2f} | "
                # Acima, estou atribuindo a variável extrato com o saldo e o ultmo valor que depositei

        else: # Condição para caso o cliente digite valores negativos para depósito
                print("Você digitou valores negativos, tente novamente")
        return self.saldo, self.extrato_deposito

class Sacar:
     
     def __init__(self, *, saque, saldo, limite_saque, VALOR_LIMITE_DE_SAQUE, extrato_saque ):
          self.saque = saque
          self.saldo = saldo
          self.limite_saque = limite_saque
          self.VALOR_LIMITE_DE_SAQUE = VALOR_LIMITE_DE_SAQUE
          self.extrato_saque = extrato_saque

     def sacar_da_conta(self):
        if self.saque >= 0: 
                if self.saque <= VALOR_LIMITE_DE_SAQUE and self.saldo >= self.saque and self.limite_saque != 3: # Condição para verificar se o limite de saque foi atingido, tem que ser diferente de 3: #Verificando se o valor do saque é até 500 e o saldo da conta tem que ser maior > saque
                    print("Saque realizado!")
                    self.saldo -= self.saque # Após a confirmação da condição, iremos fazer a subtração do saldo com o saque
                    self.limite_saque += 1 # Contador de limite de saques diários
                    self. extrato_saque += f"Saque: - R$ {self.saque:.2f} | "
                    
                elif self.saldo < self.saque: # Condicional para caso o usuario tente sacar um dinheiro que não tenha
                    print (f"Saldo indisponível para saque!") # print da mensagem e com o valor do saque. Irei adiocionar +

                elif self.saque > self.VALOR_LIMITE_DE_SAQUE: # Condicional para caso ele ultrapasse o valor limite de saque
                        print(f"Ops, o limite de saque é R${self.VALOR_LIMITE_DE_SAQUE: .2f}") 
                else:
                    print(f"Quantidade de saques diários atingido = {self.limite_saque}")     

        else:
            print(f"Error, você está tentando sacar valores negativos!") # Caso ele atinga o limite de saque diário

        return self.saldo, self.extrato_saque, self.limite_saque

class Extrato:
     
     def __init__(self, saldo, /, *, extrato_saque, extrato_deposito):
          self.saldo = saldo
          self.extrato_saque = extrato_saque
          self.extrato_deposito = extrato_deposito

     def extrato(self):
            print(f"""
        ------------ EXTRATO -----------
                  
        SALDO: R$ {self.saldo:.2f}

        {self.extrato_saque}

        --------------------------------
        
        
        {self.extrato_deposito}
         
        --------------------------------    
                    """)     
        
     
     
while True: # Estrutura de repetição while = True. Com o objetivo de ficar sempre em Loop3
    opcao = input(menu) # Exibindo a mensagem do menu e pegando a opção pelo input, atribuindo na variável opcao

    if opcao == "s": # Condição para a opção de saque
        saque = float(input("Informe o saque: R$ ")) # Após a checagem, pede o informe do saque

        saque_conta = Sacar(saque=saque, saldo=saldo, limite_saque=limite_saque, VALOR_LIMITE_DE_SAQUE= VALOR_LIMITE_DE_SAQUE, extrato_saque= extrato_saque)
        saldo, extrato_saque, limite_saque = saque_conta.sacar_da_conta()


    elif opcao == "d": # Condição para a opção de depósito que é 1 
        depositar = float(input("Informe o depósito: R$ ")) # Atribuindo o valor de depósito na variável depositar
        
        deposito_cliente = Deposito(saldo, depositar, extrato_deposito)
        saldo, extrato_deposito = deposito_cliente.depositar_em_conta()
   
    elif opcao == "e":
         extrato_da_conta = Extrato(saldo, extrato_saque=extrato_saque, extrato_deposito=extrato_deposito)
         extrato_da_conta.extrato()
         
    elif opcao == "l": # Essa condição checa se a opção 3 foi escolhida e encerrar o loop com break   
        print("Saindo do sistema...") # Mensagem de logout do sistema
        print("Obrigado por nós visitar!")
        menssagem_saida = """

        Sempre conte com nossos serviços! Estamos a sua espera. -.-

                                (͡° ͜ʖ ͡°)

        """
        print(menssagem_saida)
        break # Cortando o loop com o break
    
    elif opcao == "u": 
            cpf = int(input("CPF (Apenas números, por favor):"))

            if cpf not in lista_de_cpfs_cadastrados:
                cliente = Cliente(numero_da_conta, NUMERO_DA_AGENCIA, nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, usuarios=usuarios)
                usuarios, cpf = cliente.criar_conta()
                numero_da_conta += 1
                lista_de_cpfs_cadastrados.append(cpf)

            else:
             print(f"Aviso: Seu CPF já está cadastrado em nosso sistema")

    elif opcao == "m":
         print(usuarios)

    else: 
        print("Opção inválida, tente novamente")
              
            
    