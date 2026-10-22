# Módulos é a forma de divir seu código em vários arquivos para evitar que um arquivo de código fique enorme e para separar arquivos por responsabilidade.

# Para importar um arquivo, utiliza-se o import:
import funcoes

# Ao importar um arquivo da para utilizar as funcões dentro dela:

funcoes.saudacao("Kleber") # Para utilizar uma função é necessário passar o nome do arquivo e a função.

# OBS.: O python só reconhecer módulos quando se é um arquivo python e está na mesma pasta do arquivo principal.

# A forma de buscar módulo de outra pasta é utilizando o modelo abaixo:

    # from <nome da pasta> import <arquivo>
    
from funcoes import atv01

    # Neste exemplo não irá funcionar devido o arquivo não está dentro da pasta que está os outros arquivos, é necessário que a pasta esteja dentro dos arquivos indexavel.

# Para importar funções diretamente do arquivo, da para utilizar o método abaixo:

from funcoes import saudacao

saudacao("Nome") # Não é necessário passar o nome do arquivo.

# da para importar mais funções de uma só vez:

from funcoes import soma, subtracao

soma(1, 2)
saudacao( 4, 2)

# para importar tudo do arquivo da para fazer da seguinte forma:

from funcoes import *
    # Cuidado que este modo importa também as variáveis do código