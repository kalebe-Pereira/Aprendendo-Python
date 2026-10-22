from perfil import usuario, validacao

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if validacao.idade_valida(idade):
   print(usuario.criar_perfil(nome, idade))
else:
    print("Acesso negado!")