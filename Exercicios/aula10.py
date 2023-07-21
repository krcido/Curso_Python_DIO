# Operador de identidade

curso = " Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# verifica se as posicoes na memoria RAM sao as mesmas
# retorna um valor booleano, neste caso true
print(curso is nome_curso)

print(saldo is limite)

# negacao da afirmacao anterior

print(saldo is not limite)
 # vai dar faldo porque a negacao de verdadeiro e falso