# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).

# Quando o usuário digitar 0, o programa para e mostra o total economizado.


cofrinho = list()

while True:
    cofrinho.append(float(input("Digite algum valor: ")))
    
    if cofrinho == 0:
        break
    
    digitado = cofrinho[-1]
    
print(f"Valor economizado: R$ {sum(cofrinho)}")