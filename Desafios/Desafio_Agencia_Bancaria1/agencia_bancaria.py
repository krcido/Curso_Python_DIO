import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.nome = "Carlos"
        self.sobrenome = "Miguel da Silva"
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        data_hora = datetime.datetime.now()
        self.depositos.append((valor, data_hora))

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.saldo >= valor and len(self.saques) < 3 and valor <= 500:
            self.saldo -= valor
            data_hora = datetime.datetime.now()
            self.saques.append((valor, data_hora))
        else:
            print("Não foi possível realizar o saque.")

    def extrato(self):
        print(f"Extrato para: {self.nome_completo}")
        print("Data/Hora\t\t\tOperação\tValor")
        print("--------------------------------------------------------------")
        for valor, data_hora in self.depositos:
            print(f"{data_hora}\tDepósito\tR$ {valor:>10,.2f}")
        for valor, data_hora in self.saques:
            print(f"{data_hora}\tSaque\t\tR$ {valor:>10,.2f}")
        print("--------------------------------------------------------------")
        print(f"Saldo atual em conta: R$ {self.saldo:,.2f}")


def main():
    banco = Banco()

    while True:
        print("\n== Menu ==\n"
              "1. Depositar\n"
              "2. Sacar\n"
              "3. Imprimir Extrato\n"
              "4. Sair\n")

        try:
            opcao = int(input("Selecione uma opção: "))

            if opcao == 1:
                valor = float(input("Digite o valor a depositar: "))
                banco.deposito(valor)
            elif opcao == 2:
                valor = float(input("Digite o valor a sacar: "))
                banco.saque(valor)
            elif opcao == 3:
                banco.extrato()
            elif opcao == 4:
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
