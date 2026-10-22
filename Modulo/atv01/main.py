# Desafio 1 – Separando funções por categoria
# Crie um arquivo matematica.py com as funções:

# dobro(numero) → retorna o dobro

# metade(numero) → retorna a metade

# Crie outro arquivo mensagens.py com a função:

# boas_vindas(nome) → imprime uma mensagem de saudação

# No arquivo principal (main.py):

# Importe as funções dos dois arquivos

# Peça ao usuário um número e mostre o dobro e a metade

# Dê boas-vindas usando o nome digitado

# Desafio 2 – Criando um pacote de utilidades
# Crie uma pasta chamada meu_pacote

# Dentro dela, crie:

# formatador.py → função caixa_alta(texto) → retorna o texto em letras maiúsculas

# numeros.py → função eh_par(numero) → retorna True se for par

# No main.py:

# Importe e use as funções do pacote

# Exiba o resultado formatado

import matematica, mensagem

nome = input("Digite seu nome: ")

num = float(input("Digite o um número: "))


mensagem.boas_vindas(nome)

print(f" Metade: {matematica.metade(num)}")
print(f"Dobro: {matematica.dobro(num)}")

