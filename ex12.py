
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} Saldo atual: R${self.saldo:.2f}")

        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("João")

conta.depositar(100)
conta.sacar(150)
conta.sacar(50)
