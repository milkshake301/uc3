class Cachorro:
    #Método Contructor
    def __init__(self, nome, tamanho, raca, cor_pelo): #atributos da classe
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.cor_pelo = cor_pelo
        self.patas = 4


zeca = Cachorro("Zeca", "Médio", "Vira-lata", "caramelo")
brutus = Cachorro("Brutus", "Grande", "Pitbull", "preto")
mel = Cachorro("Mel", "Pequeno", "yorkshire", "Marrom")

zeca.patas = 3

print(zeca.nome)



class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def mudar_nome(self):
        self.nome = input("Digite o novo nome do usuário: ")    

usuario = Usuario("joão", "aleatorio@gmail.com")

usuario.desativar()

print(usuario.ativo)
