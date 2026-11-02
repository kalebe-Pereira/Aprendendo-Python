# Crie uma função leiaInt() e leiaFloat() no programa, caso não de erro na leitura informa e ao usuário.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO: Digite um valor inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mERRO: O usuário interrompeu o programa.\033[m")
            return 0
        return n
    

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(TypeError, ValueError):
            print("\033[31mERRO: Digite um valor com casas decimais válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mERRO: O usuário interrompeu o programa.\033[m")
            return 0
        return n
            
    
a = leiaInt("Digite um valor inteiro: ")
b = leiaFloat("Digite um valor Real: ")

print(f"Valor inteiro: {a}\nValor Real: {b}")
        