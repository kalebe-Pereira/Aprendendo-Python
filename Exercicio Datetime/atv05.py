# Exercício 5 – Verificador de evento
# Peça ao usuário que digite uma data de um evento

# Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

def verificar_evento(data):
    from datetime import datetime

    data = datetime.strptime(data, "%d/%m/%Y")
    hoje = datetime.now()
    
    if data.date() == hoje.date():
        print("O evento é hoje.")
    if data < hoje:
        dia_evento = hoje - data
        print(f"O evento já aconteceu a {dia_evento.days} dias.")
    if data > hoje:
        dia_evento = data - hoje
        print(f"Faltam {dia_evento.days} dias para o evento.")
    

data = input("Digite uma data: ")

verificar_evento(data)