class Cliente:
    def __init__(self, nome, sobrenome, idade, sexo, raca):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.raca = raca

    def mostrar_informacoes_cliente(self):
        print(f'Nome do cliente : {self.nome} {self.sobrenome}\nIdade : {self.idade}\nSexo : {self.sexo}\nRaça : {self.raca}')

class Conta(Cliente):
    def __init__(self, nome, sobrenome, idade, sexo, raca, numero_conta, tipo_conta):
        super().__init__(nome, sobrenome, idade, sexo, raca)
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0
    
    def mostrar_informacoes_cliente(self):
        super().mostrar_informacoes_cliente()
        print(f'Número da conta : {self.numero_conta}\nTipo da conta : {self.tipo_conta}')

    def extrato(self):
        print(f'Saldo atual : {self.saldo}')

    def sacar(self, valorSaque):
        if self.saldo < valorSaque:
            raise ValueError('O cliente não possui valor suficiente para completar a transação.')
        else:
            self.saldo -= valorSaque

    def depositar(self, valorDeposito):
        self.saldo += valorDeposito

novo_usuario = None  # Inicializa variável antes do loop

while True:
    try:
        opcao = int(input('Escolha uma das seguintes opções:\n1 - Cadastrar Cliente\n2 - Listar dados do usuário\n3 - Sair\n'))

        if opcao == 1:
            nome_novo_usuario = input('Informe o nome do novo usuário: ')
            sobrenome_novo_usuario = input('Informe o sobrenome do novo usuário: ')
            idade_novo_usuario = int(input('Informe a idade do novo usuário: '))
            sexo_novo_usuario = input('Informe o sexo do novo usuário: ')
            raca_novo_usuario = input('Informe a raça do novo usuário: ')
            novo_usuario = Cliente(nome_novo_usuario, sobrenome_novo_usuario, idade_novo_usuario, sexo_novo_usuario, raca_novo_usuario)
            print("Usuário cadastrado com sucesso!")

        elif opcao == 2:
            if novo_usuario is None:
                print("Nenhum usuário cadastrado ainda.")
            else:
                novo_usuario.mostrar_informacoes_cliente()

        elif opcao == 3:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida, tente novamente.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a opção ou idade.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
