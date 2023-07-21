# estruturas condicionais

# Estrutura if

idade = int(input("Digite a sua idade: "))

if(idade >= 18):
    print("Voce pode retirar sua CNH")
else:
    print("Voce nao pode tirar sua CNH")


# if/elif/else
opcao = int(input("Digite uma opcao: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor para o saque: "))
elif opcao == 2:
    print("Exibindo o Extrato ...")
else:
    sys.exit("Opcao invalida")