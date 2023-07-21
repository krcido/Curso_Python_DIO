# metodos de lista

# 1 - append - adiciona elementos na lista
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 50, 60])

print(lista)

# 2 - clear - para limpar a lista

lista = [1, "Python", [40,30,20]]

print(lista)

lista.clear()
print(lista) # []

# 3 - copy - copia os elemntos da lista

lista = [1, "Python", [40,30,20]]

lista2 = lista.copy()

print(lista2)

# 4 - count -contar quantas vezes um valor aparece dentro de uma lista

numeros = [1,3,1,45,23,1,2,56,1,2,3,]

print(numeros.count(1)) # 4

# 5 - extend - adiciona objetos na lista

idiomas = ["alemao, frances, portugues"]
print(idiomas)

idiomas.extend(["mandarim", "japones"])
print(idiomas)

# 6 - index - acha o indice de um objeto dentro da lista

idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(idiomas.index("frances")) # 1

# 7 - pop - retira da lista o ultimo elemento 

idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(idiomas.pop())

# 8 - remove - tambem serve para retirar elementos de uma lista
idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(idiomas.remove("frances"))

# 9 - reverse  - troca os elementos de uma lista de tras pra frente 
idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(idiomas.reverse())

# 10 - sort - ordena os elemntos de uma listapor ordem alfabetica
idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(idiomas.sort())

# ordena em ordem alfabetica de tras pra frente 
print(idiomas.sort(reverse=True))

# ordena a lista de acordo com o tamanho da string usando a funcao anonima lanbda onde o argumento x (cada elento da lista) sera verificado seu tamanho com a funcao len()
print(idiomas.sort(key=lambda x: len(x)))

# mesma coisa mas de tras pra frente
print(idiomas.sort(key=lambda x: len(x), reverse=True))

# 11 len - verifica o tamanho da lista
idiomas = ["alemao, frances, portugues","mandarim", "japones"]
print(len(idiomas))


