# Exercício 1 – Criando estrutura de pastas
# Crie a seguinte estrutura:

# ├──dados/
# │  ├── entrada/
# │  └── saida/
# ├──relatorios/
# Crie todas as pastas em uma única execução do seu código.


from pathlib import Path

dados = Path("dados/entrada")
saida = Path("dados/saida")

relatorio = Path("relatorios")

dados.mkdir(exist_ok=True, parents=True)
saida.mkdir(exist_ok=True, parents=True)
relatorio.mkdir()