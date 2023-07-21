import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.nome_completo = f"{self.nome} {self.sobrenome}"
        self.contas = []

class Conta:
    numero_conta_sequencial = 1
    AGENCIA = "0001-1"

    def __init__(self):
        self.numero_conta = f"{Conta.numero_conta_sequencial:04d}"
        Conta.numero_conta_sequencial += 1
        self.agencia = Conta.AGENCIA
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        data_hora = datetime.datetime.now()
        self.depositos.append((valor, data_hora))
        return "Depósito realizado com sucesso."

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.saldo >= valor and len(self.saques) < 3 and valor <= 500:
            self.saldo -= valor
            data_hora = datetime.datetime.now()
            self.saques.append((valor, data_hora))
            return "Saque realizado com sucesso."
        else:
            return "Não foi possível realizar o saque."

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Agência: {self.agencia}")
        print("Data/Hora\t\t\tOperação\tValor")
        print("--------------------------------------------------------------")
        for valor, data_hora in self.depositos:
            print(f"{data_hora}\tDepósito\tR$ {valor:>10,.2f}")
        for valor, data_hora in self.saques:
            print(f"{data_hora}\tSaque\t\tR$ {valor:>10,.2f}")
        print("--------------------------------------------------------------")
        print(f"Saldo atual em conta: R$ {self.saldo:,.2f}")

class Banco:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, cliente):
        cliente_existente = self._cpf_existente(cliente.cpf)
        if cliente_existente:
            novo_numero_conta = Conta.numero_conta_sequencial
            conta = Conta()
            conta.numero_conta = f"{novo_numero_conta:04d}"
            Conta.numero_conta_sequencial += 1
            cliente_existente.contas.append(conta)
            print(f"Cliente {cliente.nome_completo} já cadastrado. Nova conta vinculada:")
            print(f"CPF: {cliente.cpf}")
            print(f"Conta {conta.numero_conta} - Agência: {conta.agencia}")

        else:
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nome_completo} cadastrado com sucesso.")
            print(f"CPF: {cliente.cpf}")
            print(f"Data de Nascimento: {cliente.data_nascimento}")
            print("Endereço:")
            print(f"Logradouro: {cliente.endereco['logradouro']}")
            print(f"Número: {cliente.endereco['numero']}")
            print(f"Bairro: {cliente.endereco['bairro']}")
            print(f"Cidade: {cliente.endereco['cidade']}")
            print(f"Estado: {cliente.endereco['estado']}")

            conta = Conta()
            cliente.contas.append(conta)
            print(f"Conta {conta.numero_conta} - Agência: {conta.agencia} vinculada ao cliente.")

    def _cpf_existente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta(self, agencia, numero_conta):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.agencia == agencia and conta.numero_conta == numero_conta:
                    return conta
        return None

    def consultar_cliente(self, cpf):
        cliente_encontrado = False
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                cliente_encontrado = True
                print(f"Informações do cliente {cliente.nome_completo}:")
                print(f"CPF: {cliente.cpf}")
                print(f"Data de Nascimento: {cliente.data_nascimento}")
                print("Endereço:")
                print(f"Logradouro: {cliente.endereco['logradouro']}")
                print(f"Número: {cliente.endereco['numero']}")
                print(f"Bairro: {cliente.endereco['bairro']}")
                print(f"Cidade: {cliente.endereco['cidade']}")
                print(f"Estado: {cliente.endereco['estado']}")
                print("Contas:")
                for conta in cliente.contas:
                    print(f"Conta {conta.numero_conta} - Agência: {conta.agencia}")
                print("--------------------------------------------------")

        if not cliente_encontrado:
            print("Cliente não encontrado.")

    def listar_clientes(self):
        print("Lista de clientes cadastrados:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome_completo}, CPF: {cliente.cpf}")
            print(f"Data de Nascimento: {cliente.data_nascimento}")
            print("Endereço:")
            print(f"Logradouro: {cliente.endereco['logradouro']}")
            print(f"Número: {cliente.endereco['numero']}")
            print(f"Bairro: {cliente.endereco['bairro']}")
            print(f"Cidade: {cliente.endereco['cidade']}")
            print(f"Estado: {cliente.endereco['estado']}")
            for conta in cliente.contas:
                print(f"Conta {conta.numero_conta} - Agência: {conta.agencia}")
            print("--------------------------------------------------")

    def excluir_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nome_completo} excluído com sucesso.")
                return
        print("Cliente não encontrado.")

def menu_cliente(banco):
    while True:
        agencia = input("Digite o número da agência: ")
        numero_conta = input("Digite o número da conta: ")

        conta = banco.buscar_conta(agencia, numero_conta)
        if conta:
            print(f"Bem-vindo(a), titular da Conta {conta.numero_conta} - Agência: {conta.agencia}")
            while True:
                print("\n== Menu Cliente ==\n"
                      "1. Depositar\n"
                      "2. Sacar\n"
                      "3. Imprimir Extrato\n"
                      "4. Voltar ao Menu Principal\n")

                try:
                    opcao = int(input("Selecione uma opção: "))

                    if opcao == 1:
                        valor = float(input("Digite o valor a depositar: "))
                        print(conta.deposito(valor))
                    elif opcao == 2:
                        valor = float(input("Digite o valor a sacar: "))
                        print(conta.saque(valor))
                    elif opcao == 3:
                        conta.extrato()
                    elif opcao == 4:
                        print("Voltando ao Menu Principal.")
                        break
                    else:
                        print("Opção inválida. Por favor, selecione uma opção válida.")

                except ValueError as e:
                    print(f"Erro: {e}")
            break
        else:
            print("Agência ou conta inválida. Por favor, tente novamente.")

def menu_funcionario(banco):
    while True:
        print("\n== Menu Funcionário ==\n"
              "1. Cadastrar Cliente\n"
              "2. Consultar Cliente\n"
              "3. Listar Clientes\n"
              "4. Excluir Cliente\n"
              "5. Voltar ao Menu Principal\n")

        try:
            opcao = int(input("Selecione uma opção: "))

            if opcao == 1:
                nome = input("Digite o nome do cliente: ")
                sobrenome = input("Digite o sobrenome do cliente: ")
                cpf = input("Digite o CPF do cliente (XXX.XXX.XXX-XX): ")
                data_nascimento = input("Digite a data de nascimento do cliente (DD/MM/AAAA): ")
                logradouro = input("Digite o logradouro do cliente: ")
                numero = input("Digite o número do cliente: ")
                bairro = input("Digite o bairro do cliente: ")
                cidade = input("Digite a cidade do cliente: ")
                estado = input("Digite a sigla do estado do cliente (XX): ")

                endereco = {
                    "logradouro": logradouro,
                    "numero": numero,
                    "bairro": bairro,
                    "cidade": cidade,
                    "estado": estado.upper()
                }

                cliente = Cliente(nome, sobrenome, cpf, data_nascimento, endereco)
                banco.cadastrar_cliente(cliente)

            elif opcao == 2:
                cpf = input("Digite o CPF do cliente (XXX.XXX.XXX-XX): ")
                banco.consultar_cliente(cpf)

            elif opcao == 3:
                banco.listar_clientes()

            elif opcao == 4:
                cpf = input("Digite o CPF do cliente (XXX.XXX.XXX-XX): ")
                banco.excluir_cliente(cpf)

            elif opcao == 5:
                print("Voltando ao Menu Principal.")
                break

            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

        except ValueError as e:
            print(f"Erro: {e}")

def main():
    banco = Banco()

    while True:
        print("\n== Menu ==\n"
              "1. Acesso Cliente\n"
              "2. Acesso Funcionário\n"
              "3. Sair\n")

        try:
            opcao = int(input("Selecione uma opção: "))

            if opcao == 1:
                menu_cliente(banco)

            elif opcao == 2:
                menu_funcionario(banco)

            elif opcao == 3:
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
