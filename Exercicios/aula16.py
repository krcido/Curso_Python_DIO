#Interpolacao de variaveis

# 1 - Inerpolacao com sinal de % - Metodo antido
nome = "Guilherme"
idade = 28
profissao = "estagiario"
especializacao = "Arquitetura"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. " % (nome, idade, profissao, especializacao))
""" %s - para valores do tipo string
    %d - para valores do tipo inteiro
    %f - para valores do tipo float"""

# 2 - Interpolacao com sinal de {} - Metodo format
nome = "Guilherme"
idade = 28
profissao = "estagiario"
especializacao = "Arquitetura"

print("Ola, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, especializacao))

print("Ola, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(especializacao, profissao, idade, nome))
# Aqui e passado como argumento nas {} o index da variavel dentro da funcao format()


# 2 - Interpolacao com sinal de f - Metodo f-string
PI = 3.14159
print(f"Valor de PI:  {PI:.2f}")
print(f"Valor de PI:  {PI:10.2f}")
#O valor 10 e o numero de esapco em branco a erquerda do numero e o 2f e  numero de casas depois da virgula