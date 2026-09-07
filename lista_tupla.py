# -------------------- LISTAS ----------------------------
            
# A lista é utilizada para armazenar vários valores em uma unica variável, ela pode ser iniciada com uma abertura de couchetes.

lista = []

# Você pode adicionar valores a lista em sua declaração. Ex.:
frutas = ["maçã", "banana", "tomate" ]

# Na lista, cada item possui um endereço, começando do 0, por exemplo, a maçã é o índice 0, a banana é o índice 1 e o tomate e o índice 2. Ou seja, caso eu queira imprimir a informação de um valor na lista, utiliza-se o índice dela.

print(frutas[2])

# Caso queira saber o índice de um valor, pode-se utilizar o método. index e passando o valor como parâmetro. Exemplo:
print(frutas.index('banana'))

# A lista pode armazenar diferentes tipos de dados:
lista2 = [1 , 2, 3.14, 'Banana', True, 1]

print(lista2)

# Caso eu queira saber a quantidade de vezes que algum dados tem na lista, basta utilizar  o método .count. Exemplo:
lista2.count(1)

# Para adicionar valores na última posição da lista, utiliza-se o .append. Exemplo:
frutas.append('Abacaxi')
print(frutas)

# Para adicionar valores em qualquer lugar da lista, pode-se utilizar .insert. Exemplo:
frutas.insert(2, 'Uva') # Insere valores entre 0 e 1, empurra o da posição 1 para a 2.
print(frutas)

# Para remover valorem em uma lista, utiliza-se o .remove. Exemplo:
frutas.remove("maçã")
print(frutas)

# Para remover valores a partir do index, utiiza-se o .pop. Exemplo:
frutas.pop(0)
print(frutas)
    # No pop, da pra armazenar o valor da fruta removida:
fruta_removida = frutas.pop() # Ao não passar um index, ele remove o último valor
print(f'A fruta removida foi {fruta_removida}')

# Para alteração de algum valor, pode ser feita utilizando o índice do valor. Exemplo:
frutas[1] = 'Jabuticaba'
print(frutas)

# Para verificar a quantidade de valor em uma lista, pode se usar o método len:
print(len(frutas))

        # ----TRATAMENTOS NAS LISTAS----
      
lista = ['Abelha', 'Lobo', 'Cavalo', 'Bode', 'Elefante']
  
# Para ordenar listas no python, pode-se utilizar o método .sort, que por padrão organiza em ordem alfabética:
lista.sort()
print(lista)

# Para limpar toda a lista, utiliza-se o método .clear. Exemplo:
frutas.clear()
print(frutas)


# -------------------- TUPLAS ----------------------------

# Por fim, as tuplas são basicamente as listas, mas com a caracterista de ser imultável. Logo, qualquer método acima que não altere a estrutura da tupla pode ser utilizada. 
# Exemplo:
#   - Copy
#   - Cout
#   - Index