# Declaração de classe: 

class Garfanhoto:
    def __init__(self): # Método Construtor.
        # Atributos de Instância:
        self.nome = ''
        self.idade = 0

    # Metodos de instância:
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f"{self.nome} é Garfanhoto(a) e tem {self.idade} anos."

# Declaração de Objetos:

g1 = Garfanhoto()

g1.idade = 17
g1.nome = "Kleber"
g1.aniversario()
print(g1.mensagem())

g2 = Garfanhoto()

g2.idade = 20
g2.nome = "Maria"
print(g2.mensagem())