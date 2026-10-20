# Crie uma função chamada verificar_par(numero) que retorna:

# "Par" se o número for par

# "Ímpar" se for ímpar

# Peça um número ao usuário com input(), chame a função e mostre o resultado.

def verifica_par(numero):
    if numero % 2 == 0:
        return "Par"
    return "Ímpar"

num = int(input("Digite um número: "))
print(verifica_par(num))