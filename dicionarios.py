# Dicionários funcionam de forma similar a listas, mas elas possuiem chave e valor, que fica de fácil acesso o valor com a pesquisa da chave.
# Ao adicionar um valor, atribui-se uma chave para identificar o dado, ao invés do índice. Exemplo:

dicionario = {} # O dicionário é através de chaves.

# Para adicionar um nome de  alguém:

dicionario = {
    'nome': 'Kleber',
    'cidade': 'Brasília',
    'linguagem': 'Python'
}

# Ao adicionar os valores, os operadores para busca são a chave definida:
print(dicionario['nome'])# Similar a lista, ao invés de ser index 0, é a chave 'nome'.
print()

# Para adicionar valores (Criou-se a chave 'Data' agora):
dicionario['Data'] ='24/10/2026'

# Para alterar valores, utiliza-se a chave para acessar o valor:
dicionario['nome'] = 'Kalebe'
print(dicionario)
print()

# para apagar, utiliza-se o operador del:
del dicionario['linguagem']

    # Outra forma de apagar é utilizando o pop, da para armazenar o valor excluido em uma variável de mesmo modo das listas:
item_removido = dicionario.pop('Data')
print(f'Valor removido: {item_removido}')
print()

# No Python, da para juntar diversar formar, como por exemplo utilizar listas em um dicionário:
dicionario.update({'Profissões': ['Marcineiro', 'Design', 'Programador', 'Repositor']})

    # Para acessar os valores em lista, primeiro você acessa a chave e depois acessa o index em lista:

print(dicionario['Profissões'][2])
print()

# Para verificar as chaves do dicionário é através do método .keys():
print(dicionario.keys())
print()

    # O método keys não é possível retornar somente uma chave, mas da para alterar isso salvando os resultados em uma lista:
keys =  list(dicionario.keys())
print(keys[0])
print()    

# De forma parecida, para acessar os valores é através do método .values():
print(dicionario.values())
print()

  # O método values não é possível retornar somente uma chave, mas da para alterar isso salvando os resultados em uma lista:
values =  list(dicionario.values())
print(values[0])
print()

# Agora, para retornar valores e chaves é através do método items:
print(dicionario.items())
print()

# Para puxar valores da lista sem erro caso ela não exista, utiliza-se o .get:
print(dicionario.get('idade')) # Caso não exista, retorna-se 'None' (Vazio)
print()

    # Caso eu queira deixar uma mensagem se não existir o valor, basta escrever ao lado da função:
print(dicionario.get('idade', 'Não existe'))
