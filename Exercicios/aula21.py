# Conjuntos

# 1 - set - elimina os valores duplicados de uma lista

numeros = [1,1,2,2,3,3,4,4,]
print(set(numeros))

# convertendo o set em uma lista

numeros = {1,2,3,2}
numeros = list(numeros)

numeros[1] #2

# 2 - metodo union
a = {1,2}
b = {3,4}
print(a.union(b))

# 3 - metodo intersection
a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))

# 4 - metodo difference
a = {1,2,3}
b = {2,3,4}
print(a.difference(b))
print(b.difference(a))

# 5 - metodo symmetric_difference - retorna todos os elemtos que nao estao na interseccao
a = {1,2,3}
b = {2,3,4}
print(a.symmetric_difference(b))

# 6 - metodo issubset - retorna um valor booleano que compara se todos os elementos de um conjunto estao em outro conjunto (verifica se e um subconjunto)

a = {1,2,3}
b = {1,2.3,4,5}

# todos os elemntos de b estao em a? falso
print(a.issuperset(b)) #false

# todos os elemntos de a estao em b? verdadeiro
print(b.issuperset(a)) #true


# 7 - metodo isdisjoint - verifica se dois conjuntos sao totalemnte diferentes um do outro

a = {1,2,3,4,5}
b = {6,7,8,9}
c = {1,0}

print(a.isdisjoint(b)) #true
print(a.issuperset(c)) #false

# metodo add - adiciona um elemnto

a = {1,2,3,4,5}
print(a)
print(a.add(6))


