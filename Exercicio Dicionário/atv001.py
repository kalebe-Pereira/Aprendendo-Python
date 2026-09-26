# Crie um dicionário chamado livro com as chaves: "titulo", "autor" e "ano".

livros = dict()

livros['titulo'] = 'Estrutura de Dados'
livros['autor'] = 'Thiago Leite e Carvalho'
livros['ano'] = 2023

for k, v in livros.items():
    print(f"{k}: {v}")
