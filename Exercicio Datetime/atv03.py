# Exercício 3 – Assinatura digital do terminal
# Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

# Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02
# A data e horário devem ser do momento atual da assinatura

def assinatura(nome):
    from datetime import datetime
    agora = datetime.now()

    print(agora.strftime(f"Assiatura gerada por {nome} em %d de %B de %Y às %H:%M"))
    
assinatura("Kleber")
    
