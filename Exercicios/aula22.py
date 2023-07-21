# Dicionario - utiliza uma relacao de chave:valor para construir uma ordenacao de varios objetos

# tres formas de fazer
pessoa = {"nome": "Eduardo", "idade": 28}

pessoa = dict(nome= "Eduardo", idade = 29)

pessoa["telefone"] = "3333-1234"

# Dicionario aninhado 

agenda = {
    "contato1": {"nome": "Ana", "telefone": "1234567890"},
    "contato2": {"nome": "João", "telefone": "9876543210"},
    "contato3": {"nome": "Maria", "telefone": "4567890123"},
    "contato4": {"nome": "Pedro", "telefone": "7890123456"}
}

# tem a estrutura de um registro de dados e e muito utilizado em BD

# acesso aos registros 

{'contato1': {'nome': 'Ana', 'telefone': '1234567890'}, 'contato2': {'nome': 'João', 'telefone': '9876543210'}, 'contato3': {'nome': 'Maria', 'telefone': '4567890123'}, 'contato4': {'nome': 'Pedro', 'telefone': '7890123456'}}

