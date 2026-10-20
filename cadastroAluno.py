alunos = []

def adicionarAluno():
    print('\n' + "-" * 5 + "ADICIONAR ALUNO" + '-' * 5 + '\n')
    
    nome = input("Digite o nome do aluno: ")
    while True:
        idade = int(input("Digite a idade do aluno: "))
        if idade >= 0:
            break
        print("Idade inválida, digite novemente")
    
    while True: 
        nota = float(input("Digite a nota: "))
        if nota >= 0 and nota <= 10:   
            break
        print("Nota inválida, digite novamente.")
    
    dados = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }
    alunos.append(dados)
    
    
def listarAluno():
    print('\n' + "-" * 5 + "LISTAR ALUNO" + '-' * 5 + '\n')

    if(len(alunos) == 0):
        print("Sem alunos cadastrados")
        return
        
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n")
    
    
def procurarAluno(nome_do_aluno):
    print('\n' + "-" * 5 + "PROCURAR ALUNO" + '-' * 5 + '\n')

    if(len(alunos) == 0):
        print("Sem alunos cadastrados.")
        return
    
    for aluno in alunos:
        if aluno['nome'].lower().strip() == nome_do_aluno.lower().strip():
            print(f"Aluno: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}")
            break
    else:
        print("Aluno não cadastrado")
            
def removerAluno(nome_do_aluno):
    print('\n' + "-" * 5 + "REMOVER ALUNO" + '-' * 5 + '\n')
    
    if(len(alunos) == 0):
        print("Sem alunos cadastrados")

    for aluno in alunos:
        if aluno['nome'].lower().strip() == nome_do_aluno.lower().strip():
            alunos.remove(aluno)
    
def mediaDosAlunos():
    print('\n' + "-" * 5 + "MEDIA DOS ALUNOS" + '-' * 5 + '\n')
    if(len(alunos) == 0):
        print("Sem alunos cadastrados")
        return

    media = 0
    for i in alunos:
        media += i['nota']
        
    print(f"A média dos alunos é {media/len(alunos):.2f}")
    
    
while True:
    print("\nMENU\n")
    print("1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair\n")
    
    opcao = int(input("Digite sua opcao: "))

    match(opcao):
        case 1:
            adicionarAluno()
        case 2:
            listarAluno()
        case 3:
            nome_aluno = input("Digite o nome do aluno: ")
            procurarAluno(nome_aluno)
            
        case 4:
            nome_aluno = input("Digite o nome para remover: ")
            removerAluno(nome_aluno)
        case 5:
            mediaDosAlunos()
        case 6:
            break
        case _:
            print("Opção inválida!")