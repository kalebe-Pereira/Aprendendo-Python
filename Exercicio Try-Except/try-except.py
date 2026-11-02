# # Nas linguagem de programação existem os erros de semântica, que são erros de digitação de um chamado ou função. Mas existem erros que não aparecem de forma visível no código, como por exemplo pedir para o usuário digitar um número e ele digita uma letra.
# # Esses erros são chamados de Exceptions (Exceção, em português) e assim como na linguagem básica, podem ser tradas no código. Mas primeiro, vou lhe mostrar como verificar os erros:


# # por exemplo, caso eu peça para divir da seguinte forma:
a = 10/ '5'

# # A IDE não apresenta nenhum erro, mas possui um erro que ao executar, o programa irá apontar. Neste caso, o terminal retornou o warning: 'TypeError: unsupported operand types(s) for /: 'int' and 'str'.

# # Ótimo, achamos o erro, é um erro de tipo, informado em TypeError. No Python existem diversos erros, mas o importante no momento é verificar qual erro é.

# # Agora, utilizaremos o Try-Exception, ele serve nestes momentos. Ao digitar o programa normalmente no campo Try, e ao tenta executar e caso retorne algum erro de execução, ele cairá no campo Except.

# # Exemplo:

try:
    a = 10
    b = int(input("Digite um número para denominador: "))
except:
    print("Programa finalizado, tipo de dado inválido.")
    
# # Agora temos: tente executar (try) se der erro (except). Mas caso der certo, onde eu coloco? Agora nestes casos, utilizamos o else. Exemplo: 

try:
    a = int(input("Númerador: "))
    b = int(input("Denominador: "))
    s = a / b
except:
    print("Programa finalizado, tivemos um erro :( ")
else:
    print(f"O resultado é {s:.2f}")

# # Agora caso o valor não seja inteiro ou o valor de b for 0 o programa finaliza.

# # Mas caso eu deseje executar um trecho independente se estiver certo ou errado? Nestes casos utilizamos o finally. Ele executa independete do resultado. Exemplo:

try:
    var = 'b'
    inp = str(input("Digite uma letra e tente adivinhar: "))
except:
    print("Valor digitado não é um texto.")
else:
    if inp == var:
        print("Acertou.")
    else:
        print("Errou.")
finally:
    print("Programa finalizado :)")

# # Obs.: Os campos else e finally são opcionais.

# # O que torna o try-except muito importante é que você pode executar mais de um except e adicionar um bloco de código para cada erro. Exemplo:

try:
    a = int(input("Númerador: "))
    b = int(input("Denominador: "))
    s = a / b
except (ValueError, TypeError): # É possível passar mais de um erro em um bloco utilizando parênteses.
    print("Programa finalizado, valor digitado não é do tipo inteiro.")
except ZeroDivisionError:
    print("Programa finalizado, não é possível dividir por zero.")
else:
    print(f"O resultado é {s:.2f}")
    
    
# É possível informar as infomações do erro utiizando a classe Exception:

try:
    a = 10 / '5'
except Exception as erro: # as significa instanciar a classe erro com o erro informado.
    print(f"Tipo de erro: {erro.__class__}")
    print(f"A causa do erro: {erro.__cause__}")