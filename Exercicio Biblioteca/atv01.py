# Crie um programa que sorteia um número inteiro entre 1 e 10 usando a biblioteca random.
# O jogador tem que tentar adivinhar esse número.
# O jogo deve continuar perguntando até o jogador acertar.

# A cada tentativa, o programa deve informar:

# "Muito alto!" se o palpite for maior que o número sorteado

# "Muito baixo!" se for menor

# "Acertou!" se for igual

# Ao final, informe quantas tentativas foram necessárias para acertar.


from random import randint

numero = randint(1, 10)

adivinhe = 0
tentativas = 0
while adivinhe != numero:

    adivinhe = int(input("Digite um número: "))

    if(adivinhe > numero):
        print("Muito alto!")
        tentativas += 1
    elif(adivinhe < numero):
        print("Muito baixo!")
        tentativas += 1
    else:
        print("Acertou!")
        
print(f"Número de tentativas: {tentativas}")