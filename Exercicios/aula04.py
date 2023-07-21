# Conversao de tipos em Python

# Convertendo inteiros em float
preco1 = 10
print(preco1, " como um numero inteiro")

preco2 = float(preco1)
print(preco2, "como um umero convertiudo para float")

divisao = preco1 / 2
print('A divisao = ', divisao, ', tem como resultado um numero do tipo float')

# Convertendo float para inteiro

preco3 = 10.30
print(preco3, 'como um numero float')

preco4 = int(preco3)
print(preco4, ', transformado em um numero dotipo inteiro')
# Ao transformar um numero para o tipo inteiro, os valores depois da virgula sao perdidos definitivamente. 

# Convertendo numeros para texto (string)

nome2 = "Joao"
idade2 = 19

nome3 = str(nome2)
idade3 = str(idade2)

print(nome3, idade3, ', transformado em string')

## Outra forma de fazer isso

texto = f'O {nome2} tem {idade2} anos de idade.'
print(texto)

## Convertendo string para numero

valor = '10.30'
print(valor, 'como uma string')

valor2 = float(valor)
print(valor2 / 2, 'e o resultado de uma conta, pois o valor foi mudado para numero' )

valor3 = int(valor2)
print(valor3)