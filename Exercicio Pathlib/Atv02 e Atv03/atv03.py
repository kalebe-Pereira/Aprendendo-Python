# Exercício 3 – Conferindo e filtrando arquivos .txt
# Liste todos os arquivos .txt dentro de entrada/.

# # Imprima apenas o nome do arquivo (sem o caminho completo).

from pathlib import Path

caminho = Path("entrada")

for arquivo in caminho.glob("*.txt"):
    print(arquivo.stem)
    