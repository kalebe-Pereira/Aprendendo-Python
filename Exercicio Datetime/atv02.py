# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

# Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!

from datetime import datetime

mes = datetime.now().month

print(f"Faltam {12 - mes} meses para acabar o ano")