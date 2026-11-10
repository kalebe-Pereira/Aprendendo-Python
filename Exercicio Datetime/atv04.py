# Exercício 6 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime

final_do_ano = datetime(2026,12,31)

contagem = final_do_ano - datetime.now()

print(f"Faltam {contagem.days} dias para o final do ano.")
