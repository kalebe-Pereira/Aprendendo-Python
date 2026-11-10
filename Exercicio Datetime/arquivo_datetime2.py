# No datetime existe também um módulo timedelta, utilizado para fazer clculos utilizando datas.

from datetime import datetime, timedelta

hoje = datetime.now()

um_dia = timedelta(days= 1) # Utilizando o timedelta para armazenar o valor referente a um dia.

# Agora é possível fazer operações matemáticas utilizando as duas variáveis:

amanha = hoje + um_dia  # Desse modo, aparecerá a data de amanhã.

print(amanha) 

# Utilizando a mesma lógica, subtrairemos 1 dia de hoje:

ontem = hoje - um_dia

print(ontem) # Data de ontem.

# OBS.: Só é possível fazer operações quando os dois valores estão no formato datetime (ou timedelta).


# ----------------------------------------------------------------------------------------------------------------

# É possível fazer comparações entre datas para alguma ocasião:

prazo = datetime(2026, 12, 31)

if hoje > prazo:
    print("Prazo vencido!")
else:
    print("Ainda está no prazo.")
# Com isso efetuamos comparações utilizando datas.

# Para efetuar comparações mais precisas, precisa-se se atentar em um modelo:

dia_aniversario = datetime(2026, 11, 10)

# para efetuar comparações de igualdade, é necessário utilizar igualdades no dia e no mês, caso contrário irá mostrar erro devido o horário:

if hoje.day == dia_aniversario.day and hoje.month == dia_aniversario.month: # Ou utilizar o date: hoje.date() == dia_aniversario.date()
    print("Hoje é seu aniversário!")
elif hoje > dia_aniversario:
    print("Seu aniversário já passou.")
elif hoje < dia_aniversario:
    print("Seu aniversário ainda vai acontecer.")

# Para ver a quantidade de dias restantes, basta subtrair as variáveis:

print(prazo - hoje)

# para obter somente os dias:

prazo_dias = prazo - hoje

print(prazo_dias.days)