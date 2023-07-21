# Listas 

# 1- Lista com valores definidos
frutas = ["Laranja", "Maca", "Uva"]

# 2 - Lista vazia
frutas = []

# 3 - lista onde cada letra e um elemento com index
letras = list("Phyton")

# 4 - lista com um range como valores
numeros = list(range(10))

# 5 - Lista com valores de diversos tipos
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]

## Aceso aos valores de uma lista

#6 - Acessar elemento maca da lista frutas
# retorna o elemnto 1 da lista que e o que queremos
frutas[1]

# 7 - Listas aninhadas - uma lista que armazena outras listas

# a) Matriz
matriz = [
    {1, "a", 2},
    {"b, 3, 4"},
    {6, 5, "c"}
]

# a.1) Buscar por linha
matriz[0] # [1, "a", 2]

# a.2) buscar um elemento especifico
# matriz [linha][coluna]
matriz[0][0] # 1

# a.3) busca por indice negativo
matriz [0][-1] # 2
matriz [-1][-1]

# 8 - Iterar Listas (Percorrer os valores)

numeros = [1,2,3,4,5,6,7]

for numero in numeros:
    print(numero)

#estrutua foreach 

#9 - Enumerar uma lista
numeros = [1,2,3,4,5,6,7]

for indice, numero in enumerate(numeros):
    print(f"Item {indice}: {numero}")

# 10 - Compressao de lista - criar uma nova lista a partir de uma lista existente

## Versao 1
numeros = [1,30,21,2,9,65,34]
#criar uma nova lista somente com os numeros pares a partir da lista numeros

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

## Versao 2
numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)