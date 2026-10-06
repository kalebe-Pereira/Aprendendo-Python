contador = 0

# O for é uma estrutura utilizada para repetições contadas. Sendo muito utilizado para percorrer listas. 
    # Exemplo:
for i in range(1, 5): # O range funciona do primeiro número ao último -1. Neste loop fica de 1 a 4
    print(i)
print()

# Percorrendo listas:
frutas = ['Maçã', 'banana', 'ameixa', 'morango', 'laranja']

for i in frutas:
    print(f'fruta: {i}')

# Escrevendo a taboada do 1 ao 10 muito mais fácil:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()




# O while é utilizado para repetições até uma certa condição específica, sendo usada para eventos de código como o botão fechar.

while(contador < 5):
    contador+= 1
    print(contador)
print()
    # Detalhe: caso não possua o incremento, o programa funcionaria para sempre.

# com o while, da para fazer verificações de acesso:

senha = ''
while senha != 'python':
    senha = input("Digite sua senha: ")

print("Senha correta!") # Só irá aparecer esse campo caso a senha digitada está correta.