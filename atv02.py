# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

numeros = list()

for i in range(5):
    numeros.append(int(input(f"Digite o {i + 1} número: ")))

print(sum(numeros))