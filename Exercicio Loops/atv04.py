# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"

# 2."Hambúrguer"

# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando

# No final, mostre quantos votos cada item recebeu


pizza = 0; hamburger = 0; opcao = 0

while opcao != 3:
    print("""
          1. Pizza
          
          2. Hambúrger

          3. Sair
    """)
    
    opcao = int(input("Digite sua opção: "))

    if(opcao == 1):
        pizza += 1
    elif(opcao == 2):
        hamburger += 1

print(f"""
      Total de votos: 
      
      Habúrger: {hamburger}
      
      Pizza: {pizza}
      
""")