class RelatorioPDF:
    def gerar(self, dados):
        print(f"Gerando arquivo PDF com os dados: {dados}...")

class RelatorioExcel:
    def gerar(self, dados):
        print(f"Gerando planilha Excel com os dados: {dados}...")


print("--- Teste Exercício 4: Polimorfismo ---")


relatorios = [RelatorioPDF(), RelatorioExcel()]


for relatorio in relatorios:
    relatorio.gerar("Vendas de Maio")