# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"

# 2."Hambúrguer"

# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando

# No final, mostre quantos votos cada item recebeu


pizza = 0; hamburger = 0; opcao = 0

while True:
    print("1. Pizza\n2. Hamburger\n3. Sair\n")
    
    opcao = int(input("Digite sua opção: "))

    match opcao:
        case 1:
            pizza+= 1
        case 2:
            hamburger+=1
        case 3:
            break
        case _:
            print("Opção Inválida!")


print(f"\nTotal de votos:\n\nHabúrger: {hamburger}\nPizza: {pizza}")