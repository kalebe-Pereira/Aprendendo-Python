# O datetime é uma biblioteca feita para acesso de datas, com ela você consegue adquirir informações de horas, dias,meses e anos. Biblioteca utilizada para automatizações.

# Para acessar o datetime, primeiro é necessário importar a classe datetime:

from datetime import datetime

agora = datetime.now() # busca a data de hoje.

print(agora) # Mostra o objeto agora.

# Neste objeto eu posso chamar os atributos de agora:

print(agora.day, end="/") # Retorna o dia.
print(agora.month, end="/") # Retorna o mês.
print(agora.year) # Retorna o ano

# Agora para buscar atributos relacionados a hora, temos:

print(agora.hour, end=":") # Retorna a hora.
print(agora.minute, end=":") # Retorna os minutos.
print(agora.second) # Retorna os segundos.

# -----------------------------------------------------------------------------------------------------------------------------

# É possível armazenar uma data utilizando o datetime:

aniversario = datetime(2000, 1, 1) # ano, mês e dia. É possível passar as horas também, basta continuar atribuindo.

print(aniversario)

# é possível utilizar o datetime para escrever uma string de forma mais otimizada, exemplo:

print(agora.strftime("Hoje é dia %d do mês %m do ano %y")) # O strftime converte a data em %d(dia), %m (mês) e %Y (ano).

# Existe o mesmo modelo relacionado ao horário:

print(agora.strftime("agora é %H horas, %M minutos e %S segundos."))

# ---------------------------------------------------------------------------------------------------------------------------

# Existe um método do datetime utilizado para ler datas, chamado agora strptime, ele torna uma data recebida em um objeto datetime:

data_aleatoria = "27/07/2015"

data_convertida = datetime.strptime(data_aleatoria, "%d/%m/%Y") # É necessário informar como está formatado a data.

print(data_convertida) # Agora data convertida está com os dados de data_aleatoria no formato datetime, podendo acessar os atributos:

print(data_convertida.day)
print(data_convertida.month)
print(data_convertida.year)
