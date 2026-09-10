class Arma:
    def __init__(self, nome_arma, dano_extra):
        self.nome_arma = nome_arma
        self.dano_extra = dano_extra

class Personagem:
    def __init__(self, id_jogador, nome):
        self.id_jogador = id_jogador
        self.nome = nome
        self.vida = 100
        self.arma_equipada = None

    def equipar(self, objeto_arma):
        self.arma_equipada = objeto_arma
        print(f"{self.nome} equipou a arma {objeto_arma.nome_arma}!")

    def atacar(self, alvo):
        dano = 10
        if self.arma_equipada:
            dano += self.arma_equipada.dano_extra
        alvo.vida -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        print(f"Vida atual de {alvo.nome}: {alvo.vida}")

# Sistema
def menu_rpg():
    armas_disponiveis = [Arma("Espada", 15), Arma("Machado", 20), Arma("Adaga", 10)]
    personagens = {}
    
    while True:
        print("\n=== Arena RPG ===")
        print("[1] Cadastrar Personagem\n[2] Listar Personagens\n[3] Selecionar Personagem\n[0] Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            id_jog = input("ID do jogador: ")
            nome = input("Nome do personagem: ")
            personagens[id_jog] = Personagem(id_jog, nome)
            print("Personagem cadastrado!")
        elif opcao == '2':
            for p in personagens.values():
                arma_nome = p.arma_equipada.nome_arma if p.arma_equipada else "Nenhuma"
                print(f"ID: {p.id_jogador} | Nome: {p.nome} | Vida: {p.vida} | Arma: {arma_nome}")
        elif opcao == '3':
            id_jog = input("ID do jogador: ")
            if id_jog in personagens:
                p = personagens[id_jog]
                while True:
                    print(f"\n--- Personagem: {p.nome} ---")
                    print("[1] Equipar Arma\n[2] Atacar\n[3] Ver Status\n[0] Voltar")
                    sub_op = input("Escolha: ")
                    
                    if sub_op == '1':
                        print("Armas disponíveis:")
                        for i, a in enumerate(armas_disponiveis):
                            print(f"[{i}] {a.nome_arma} (+{a.dano_extra} dano)")
                        escolha = int(input("Escolha o número da arma: "))
                        if 0 <= escolha < len(armas_disponiveis):
                            p.equipar(armas_disponiveis[escolha])
                    elif sub_op == '2':
                        id_alvo = input("ID do alvo: ")
                        if id_alvo in personagens and id_alvo != p.id_jogador:
                            p.atacar(personagens[id_alvo])
                        else:
                            print("Alvo inválido.")
                    elif sub_op == '3':
                        arma_nome = p.arma_equipada.nome_arma if p.arma_equipada else "Nenhuma"
                        print(f"Nome: {p.nome} | Vida: {p.vida} | Arma: {arma_nome}")
                    elif sub_op == '0':
                        break
            else:
                print("Personagem não encontrado.")
        elif opcao == '0':
            break

# menu_rpg()