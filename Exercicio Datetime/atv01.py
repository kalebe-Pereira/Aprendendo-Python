# Exercício 1 – Relógio de verificação
# Mostre a hora atual no terminal, mas com a seguinte regra:

# Se a hora for antes das 12h, imprima: "Bom dia!"

# Se estiver entre 12h e 18h: "Boa tarde!"

# Depois disso: "Boa noite!"

from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))

hora = datetime.now().hour
if hora < 12:
    print("Bom Dia!")
elif hora >= 12 and hora < 18:
    print("Boa Tarde!")
else:
    print("Boa Noite!")