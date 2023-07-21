# Manipulacao com Strings

# Metodo UPPER - converte todos os carecteres para maiusculo
string = "texto"
print(string.upper())

# Metodo LOWER - converte todos os carecteres para minusculo
string = "TEXTO"
print(string.lower())

# Metodo TITLE - converte todos os carecteres para minusculo, menos o primeiro caracter
string = "TEXTO"
print(string.title())

# Eliminando os espacos em branco da String
string = "  Oi !"
print(string.strip()) # remove os espacos da esquerda e da direita

string = "  Oi !"
print(string.rstrip()) # remove os espacos somente da direita

string = "  Oi !"
print(string.lstrip()) # remove os espacos somente da esquerda


#Centrolizacao e Juncoes de strings
texto = "Python"
print(texto.center(10,"#")) # adiciona os caracteres especificados a direita e esquerda da string
"""neste caso foi dito que somado a palavra Python, a string deve ter 
   no maximo 10 caracteres e a funcao ira completar o que falta com o caracter "#"
   mantendo o texto original no meio"""

# Juncao de strings
texto = "Python"
print(".".join(texto)) 
"""adiciona os caracteres epsecificados ao final de cada caracter da string 
menos antes e depois do primeiro e do ultimo"""
