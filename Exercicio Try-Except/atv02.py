#  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
import urllib.error

try:
    requisicao = urllib.request.Request(
        'https://www.pudim.com.br',
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )

    site = urllib.request.urlopen(requisicao, timeout=10)

except urllib.error.URLError:
    print("O site não está acessível:")

else:
    print("O site Pudim está acessível!")

