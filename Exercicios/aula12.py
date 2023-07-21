# Identacao
# Identacao e obrigatoria em Python e determina a funcionalidade do codigo na linguagem

saldo = 500
valor_a_sacar = float(input("Digite o valor para saque: "))
print("")
def sacar(saldo: float, valor_a_sacar: float):
    if saldo < valor_a_sacar:
        print("Não há saldo suficiente para essa operação.")
    else:
        saldo -= valor_a_sacar
        print("================================")
        print("Saque realizado com sucesso!")
        print("Retire seu dinheiro na bandeja.")
        print("================================\n")
        print(f"Seu saldo é de {saldo:.2f}. \n")
        print("================================\n")

# Chamando a função
sacar(saldo, valor_a_sacar)