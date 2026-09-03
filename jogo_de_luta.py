class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self.vida = 100
        self.ataque = forca

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque


gandalf = Personagem("Gandalf", 20)
sauron = Personagem("Sauron", 15)

while True:
    gandalf.atacar(sauron)

    if sauron.vida <= 0:
        print(f"{gandalf.nome} venceu!")
        break

    sauron.atacar(gandalf)

    if gandalf.vida <= 0:
        print(f"{sauron.nome} venceu!")
        break