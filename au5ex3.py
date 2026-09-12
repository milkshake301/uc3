class AssinaturaBase:
    def __init__(self, usuario):
        self.usuario = usuario

    def calcular_preco(self):
        return 0.0

class AssinaturaPremium(AssinaturaBase):
    def calcular_preco(self):
        return 49.90

class AssinaturaEstudante(AssinaturaBase):
    def calcular_preco(self):
        return 24.90

print("--- Teste Exercício 3: Herança ---")
plano_premium = AssinaturaPremium("Maria")
plano_estudante = AssinaturaEstudante("João")

print(f"Assinatura do usuário {plano_premium.usuario} custa: R$ {plano_premium.calcular_preco():.2f}")
print(f"Assinatura do usuário {plano_estudante.usuario} custa: R$ {plano_estudante.calcular_preco():.2f}")
print()