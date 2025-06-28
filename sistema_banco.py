import datetime

class Cliente:
    def __init__(self, id_cliente, nome, sobrenome, idade, sexo, raca):
        self.id_cliente = id_cliente
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.raca = raca

    def mostrar_informacoes(self):
        print(f'\nInformações do Cliente:')
        print(f'ID: {self.id_cliente}')
        print(f'Nome: {self.nome} {self.sobrenome}')
        print(f'Idade: {self.idade}')
        print(f'Sexo: {self.sexo}')
        print(f'Raça: {self.raca}')


class Conta:
    def __init__(self, cliente, numero_conta, tipo_conta):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0.0
        self.historico = []

    def extrato(self):
        print(f'\nExtrato da Conta {self.numero_conta}')
        print(f'Tipo: {self.tipo_conta}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')
        if not self.historico:
            print("Sem movimentações.")
        else:
            for item in self.historico:
                print(f"{item['data']} - {item['tipo']} - R$ {item['valor']:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        if self.saldo < valor:
            print("Saldo insuficiente para saque.")
            return
        self.saldo -= valor
        self.historico.append({
            'tipo': 'Saque',
            'valor': valor,
            'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        print("Saque realizado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return
        self.saldo += valor
        self.historico.append({
            'tipo': 'Depósito',
            'valor': valor,
            'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        print("Depósito realizado com sucesso.")

# Aplicação
clientes = {}
conta_corrente = None

while True:
    try:
        print("\n=== Menu Principal ===")
        print("1 - Cadastrar Cliente")
        print("2 - Criar Conta")
        print("3 - Mostrar Informações do Cliente")
        print("4 - Depositar")
        print("5 - Sacar")
        print("6 - Ver Extrato")
        print("7 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            id_cliente = int(input("ID do cliente: "))
            if id_cliente in clientes:
                print("ID já cadastrado.")
                continue
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ")
            raca = input("Raça: ")
            cliente = Cliente(id_cliente, nome, sobrenome, idade, sexo, raca)
            clientes[id_cliente] = cliente
            print("Cliente cadastrado com sucesso.")

        elif opcao == 2:
            if not clientes:
                print("Cadastre um cliente primeiro.")
                continue
            id_cliente = int(input("ID do cliente: "))
            cliente = clientes.get(id_cliente)
            if not cliente:
                print("Cliente não encontrado.")
                continue
            numero_conta = input("Número da conta: ")
            tipo_conta = input("Tipo da conta (Corrente/Poupança): ")
            conta_corrente = Conta(cliente, numero_conta, tipo_conta)
            print("Conta criada com sucesso.")

        elif opcao == 3:
            if conta_corrente is None:
                print("Nenhuma conta ativa.")
            else:
                conta_corrente.cliente.mostrar_informacoes()

        elif opcao == 4:
            if conta_corrente is None:
                print("Nenhuma conta ativa.")
            else:
                valor = float(input("Valor para depósito: R$ "))
                conta_corrente.depositar(valor)

        elif opcao == 5:
            if conta_corrente is None:
                print("Nenhuma conta ativa.")
            else:
                valor = float(input("Valor para saque: R$ "))
                conta_corrente.sacar(valor)

        elif opcao == 6:
            if conta_corrente is None:
                print("Nenhuma conta ativa.")
            else:
                conta_corrente.extrato()

        elif opcao == 7:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Entrada inválida. Digite corretamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
