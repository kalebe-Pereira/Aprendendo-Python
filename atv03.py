# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).

# Quando o usuário digitar 0, o programa para e mostra o total economizado.

digitado = 1
cofrinho = list()

while(digitado != 0):
    cofrinho.append(float(input("Digite algum valor: ")))
    digitado = cofrinho[-1]
    
print(f"Valor economizado: R$ {sum(cofrinho)}")