# Desafio 2 – Criando um pacote de utilidades
# Crie uma pasta chamada meu_pacote

# Dentro dela, crie:

# formatador.py → função caixa_alta(texto) → retorna o texto em letras maiúsculas

# numeros.py → função eh_par(numero) → retorna True se for par

# No main.py:

# Importe e use as funções do pacote

# Exiba o resultado formatado

import formatador, numeros

numeros = formatador.caixa_alta(numeros.eh_par(4))

print(numeros)
