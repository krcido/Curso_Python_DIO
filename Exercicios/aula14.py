# Estruturas de repeticao

# 1 - Estrutura FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
CONSOANTES = "BCDFGHJKLMNPQRSTVXWYZ"
vogais_encontradas = []
consoantes_encontradas = []
total_vogais = 0
total_consoantes = 0

for letra in texto:
    if letra.upper() in VOGAIS:
       vogais_encontradas.append(letra)
       total_vogais +=1

    if letra.upper() in CONSOANTES:
        consoantes_encontradas.append(letra)
        total_consoantes += 1

vogais_str = " - ".join(vogais_encontradas)
consoantes_str = " - ".join(consoantes_encontradas)
resultado = (
    "\nVogais encontradas na palavra: " + vogais_str +
    "\nTotal de vogais = " + str(total_vogais) +
    "\n\nConsoantes encontradas na palavra: " + consoantes_str +
    "\nTotal de consoantes = " + str(total_consoantes) + "\n"
)

print(resultado)


# 2 - Range
list(range(4))

for numero in range(11):
    num_str = " - ".join(map(str, range(numero)))
    
print(num_str)

# O join funciona apenas com string, para usa-lo com numeros antes sera preciso transformar o numero em string


# Tabuada com o range
tabuada = []
for numero in range(0, 41, 4):
    tabuada.append(numero)
# o metodo append() adiciona o item da posicao percorrida no laco for ao ultimo indice da lista []
    
print("Tabuada do 4 = ", tabuada)



## 3 - Estrutura Whiile
while True:
    show_menu()
    option = input("Escolha uma opção (1/2/3/4): ")

    if option == '1':
        deposit_amount = float(input("Digite o valor para depósito: "))
        account.deposit(deposit_amount)
    elif option == '2':
        withdraw_amount = float(input("Digite o valor para saque: "))
        account.withdraw(withdraw_amount)
    elif option == '3':
        account.print_statement()
    elif option == '4':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")