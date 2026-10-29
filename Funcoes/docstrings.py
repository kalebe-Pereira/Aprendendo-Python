# O docstring serve para verificar a documentação/ manual de uma função. É possível verificar o que uma função no python faz utilizando o método help:

help(print) # Exibi o que faz e utilização

# É possível também visualizar a dpcumentação de uma função, basta utilizar o método __doc__:

print(input.__doc__)

# Mas, caso eu queira importar minhas funções para outras pessoas,irá aparecer para as outas pessoas?

    # É para isso, que servem docstrings que servem para criar um manual nas suas próprias funcões.
    
# O Docstring é adicionado abaixo do comando def, é adicionado utilizando 3 aspas duplas:

def soma(n1, n2):
    """ -> <O que a função faz>

    Args:
        n1 (_type_): _description_
        n2 (_type_): _description_
    """
    # Esse é o modelo base de uma docstring. Onde é necessário informar o tipo para as declarações e a descrição de cada. Pode-se adicionar uma descrição mais detalhada da função, basta criar um campo description e escrever o que a funcão faz.
    return n1 + n2

# agora, se utilizar o help e a função. Irá aparecer o que está dentro das aspas.

help(soma)