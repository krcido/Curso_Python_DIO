# Input e Output - entrada e saida de valores via teclado

#Input - sempre que algo e dado como entrada de dados, por padrao vira como dado do tipo string

nome = input("Informe o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

# Output - saida dos dados entrados via Input em tela (disposito de saida)
print('Meu nome e', nome)
print(nome, sobrenome, end='...\n')
print(nome, sobrenome, sep="-")