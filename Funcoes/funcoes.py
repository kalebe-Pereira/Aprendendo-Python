# As fuções são trechos de códigos com a possibilidade de reutilização. A função tem como a reutilização ao chamar o nome declarado nela. Exemplo:

def bemVindo(): # Para declarar uma fuunção, utiliza-se o def antes do nome da função.
    print("Olá, seja bem vindo!")

# Perceba que ao declarar uma função e executar o código não irá aparecer nada, isso é devido ser necessário chamar a função para que ela execute:

bemVindo()

# Mas como reutiliza?

# Simples, basta chamar o nome da função quantas vezes você quiser.

bemVindo()
bemVindo()
bemVindo()



# Nas funções podem existir PARÂMETROS. Eles são valores passados na execução da função necessário para que ela funcione:

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem vindo.")
    
# Agora para chamar a função será necessário passar o nome da pessoa dentro dos parêntes:

saudacao("Kleber")
    
# ----- PARÂMETROS OPCIONAIS -----

    # Os parâmetros opcionais servem para caso não seja obrigatório passar outro valor para a função:
    
    # Exemplo:
    
def saudacao(nome, parametro_opcional=0):
    print(f"Oi, {nome}")
    
    if parametro_opcional != 0:
        print("Caldo de cana")
        
    # Agora, ao passar somente o nome o programa executa normalmente. Mas, caso passe o segundo parâmetro será executado o restate do código.
    
saudacao("Kleber") # Normal.
saudacao("Kleber", 1) # Paramêtro extra.

# ----- EMPACOTAMENTO ----

    # O empacotamento é a possibilidade de passar uma quantidade indetermidada de parâmetros, isso possibilita algumas coisas.
    
    # Exemplo:
    
def contador(*num): # É necessário passar o asterisco para funcionar.
    for i in num:
        print(i, end=' ')
    print(f"Total {len(num)}")
    # No *num, o parâmetro será tratado como uma tupla

contador(1, 2, 3, 5)
contador(5,6)
contador(9, 8, 6, 5, 9, 8, 7)
# Será executado normalmente.


# As funções também pode ser utilizadas para problemas lógicos:

def soma(n1, n2):
    print(f"A soma de {n1} e {n2} é igual a {n1 + n2}")
    
# Agora é necessário passar 2 parâmetros para que a função funcione:

soma(10, 24)

# Ao chamar a função ela faz o calculo dos valores passados. Caso deseje armazenar o resultado de uma função, utiliza-se o return, utilizado para retornar o valor:

def retornoSoma(num1, num2):
    return num1 + num2

# Ao executar, não aparecerá nenhum resultado, isso é porquê é necessário armazenar o resultado em uma variável:

resultado = retornoSoma(56, 89)

print(f"Resultado: {resultado}")

# ou só imprimir o valor:

print(retornoSoma(9, 5))
