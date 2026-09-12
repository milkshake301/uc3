class ProcessadorDePagamento:

    def _conectar_banco(self):
        print("Conectando ao banco de dados...")

    def _autenticar_token(self):
        print("Autenticando transação...")

    def _deduzir_saldo(self, valor):
        print(f"Deduzindo R$ {valor} do saldo...")

    def processar_compra(self, valor):
        self._conectar_banco()
        self._autenticar_token()
        self._deduzir_saldo(valor)
        print("Compra finalizada com sucesso")


print("--- Teste Exercício 2: Abstração ---")
processador = ProcessadorDePagamento()
processador.processar_compra(250.50)
print()