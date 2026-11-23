# Exercício 2 – Criar vários arquivos de exemplo
# Dentro da pasta entrada/, crie 3 arquivos vazios:

# dados1.txt

# dados2.txt

# dados3.txt

from pathlib import Path

pasta = Path("entrada")
pasta.mkdir()

dados1 = Path("entrada/dados1.txt")
dados1.touch()

dados2 = Path("entrada/dados2.txt")
dados2.touch()

dados3 = Path("entrada/dados3.txt")
dados3.touch()
