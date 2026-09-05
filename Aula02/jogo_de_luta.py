class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.vida = 100

    def atacar(self,alvo):
        alvo.vida -= self.forca

gandalf = Personagem("Gandalf", 20)
sauron = Personagem("Sauron", 15)

while True:
    gandalf.atacar(sauron)
    sauron.atacar(gandalf)

    if gandalf.vida <= 0:
        print(f"{sauron.nome} venceu")
        break

    if sauron.vida <= 0:
        print(f"{gandalf.nome} venceu")
        break
    