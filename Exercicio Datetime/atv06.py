# Exercício 6 – Validade de produto 🥫
# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.
# Mostre:

# A data de validade

# Se o produto ainda está válido ou já venceu

# Quantos dias faltam ou há quanto tempo passou do prazo


def verifica_validade(data_vencimento):
    from datetime import datetime, timedelta

    data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
    data_vencimento = data_vencimento + timedelta(days=180)
    hoje = datetime.now()
    
    print(data_vencimento.strftime("A data de vencimento é %d/%m/%Y."))

    if data_vencimento.date() == hoje.date():
        print("A data de vencimento é hoje.")
    elif data_vencimento > hoje:
        data = data_vencimento - hoje
        print(f"O produto vence daqui a {data.days} dias.")
    elif data_vencimento < hoje:
        data = hoje - data_vencimento
        print(f"O produto venceu a {data.days} dias atrás.")
        
        
        
data = input("Digite a fabricação do produto do produto: ")

verifica_validade(data)