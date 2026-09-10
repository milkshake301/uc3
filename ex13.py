class CarteiraDigital:
    def __init__(self, nome_titular, saldo_inicial):
        self.saldo = saldo_inicial
        self.nome_titular = nome_titular

    def transferir(self, valor, destinatario):
        if valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            print(f"Transferência de R${valor:.2f} para {destinatario.nome_titular} realizada com sucesso.")
        else:
            print("Saldo insuficiente para realizar a transferência.")


cliente_a = CarteiraDigital("João", 500)
cliente_b = CarteiraDigital("Mariana", 100)


cliente_a.transferir(150, cliente_b)

print(cliente_a.saldo)  
print(cliente_b.saldo)