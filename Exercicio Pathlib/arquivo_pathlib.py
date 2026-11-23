# O pathlib é utilizado para gerenciar arquivos, com as opções de mover, criar, excluir, etc.

# Para importar a biblioteca, é pelo método abaixo:

from pathlib import Path

# Path (Ou caminho) é uma localização que o seu computador usa para acessar algum arquivo através de pastas/diretórios.

caminho = Path("caminho.txt")

print(caminho)

# Ao utilizar o Path, a variável caminho agora aponta o arquivo caminho.txt.

# Existem 2 tipos de caminhos, os relativos e absolutos:

# RELATIVO: Utiliza a pasta que está o arquivo como o caminho principal e origem do path.
    # Ex.: Exercicio Pathlib/caminho.txt
    
# ABSOLUTO: Utiliza a primeira pasta do computador como caminho principal e origem do path.
    # Ex.: /home/user/Documentos/Aprendendo-Python/Exercicio Pathlib/caminho.txt

caminho_absoluto = Path(r"/home/kleber/Documentos/Aprendendo-Python/Exercicio Pathlib/caminho.txt")
# r -> Desconsidera caracteres especiais '/'

# é possível converter caminhos relativos para caminhos absolutos no pathlib, utilizando o método absolute:

caminho = caminho.absolute()

print(caminho)

# ---------------------------------------------------------------------------------------------------------

# É possível verificar se o caminho existe:

caminho = Path("caminho.txt")
if caminho.exists():
    print("Existe!")
else:
    print("Não existe!")
    
    
# e para verificar se é um arquivo ou uma pasta:
if caminho.is_file():
    print("É arquivo")
elif caminho.is_dir():
    print("É uma pasta")

#-----------------------------------------------------------------------------------------------------------

    # --------- CRIAR PASTA ---------
    
# É possível criar uma pasta através do pathlib da seguinte forma:

nova_pasta = Path("Pasta Exemplo") # Nome da pasta dentro  dos parenteses. 

nova_pasta.mkdir(exist_ok=True) # O mkdir é o comando para criação de pasta.
    # O exist_ok é para não dar flag caso a pasta já exista.
    
# Para criar pastas dentro de pastas é da seguinte forma: 

nova_pasta = Path("Pasta Exemplo/Outra Pasta/Mais uma Pasta") # Adicione o caminho dentro da pasta.
nova_pasta.mkdir(exist_ok=True,parents=True) # parents serve para que seja possível criar pastas dentro de outras pastas


    # --------- DELETAR PASTA ---------

# É possível deletar arquivos através do método unlink:

caminho.unlink(missing_ok=True) # unlink para deletar arquivos.
    # missing_ok serve para ignorar caso o arquivo já esteja deletado.
    
nova_pasta.rmdir() #rmdir para pastas.
    #rmdir só para pastas vazias.

 
    # --------- LER ARQUIVO ---------

# Para ler arquivos, existe um método para leitura (É recomendado utilizar outra biblioteca só para leitura, utilizar essa somente para verificação rápida):

arquivo = Path("arquivo.txt")
print(arquivo.read_text())

# Para escrever nesse arquivo, utilize o método write_text:

arquivo.write_text("Alterando o texto do arquivo", encoding="utf-8") # Enconding serve para aceitar caracteres especiais do utf-8.
print(arquivo.read_text())
# Após execução, o texto anterior da pasta é substituido por esse.

    #  --------- VERIFICAR ARQUIVOS ARQUIVO ---------

pasta = Path("Pasta Exemplo")

for arquivo in pasta.iterdir(): # Intera por diretório.
    print(arquivo)
    # Isso verifica os arquivos existente na pasta 'Pasta Exemplo'.
    
# Para verificar os arquivos da pasta root (Parta onde o arquivo está armazenado) é só não informar um caminho no Path:

pasta_principal = Path()
for arquivo in pasta_principal.iterdir():
    print(arquivo)
    
# ----------------------------------------------------------------

# Para filtrar o retorno para só um tipo de dado, utiliza-se o .gob():

for arquivo in pasta_principal.glob("*.txt"): # O formato é: *.<tipo_do_arquivo>
    print(arquivo)

# Para verificar os arquivos, primeiro devemos ter um meio de visualizar-lo separadamente:

arquivo = Path("Pasta Exemplo/Arquivo modelo.txt")
arquivo.touch() # O touch cria o arquivo.

# Para verificar, temos as seguintes opções:

print(arquivo) # Retorna o caminho.
print(arquivo.name) # Retorna somente o nome do arquivo com a extensão.
print(arquivo.stem) # Retorna somente o nome do arquivo.
print(arquivo.suffix) # Retorma somente a extensão do arquivo.

