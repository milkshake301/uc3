class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def salvar_no_banco(self):
    # O chamador NÃO precisa saber:
    # - Como a conexão SQL é aberta
    # - Qual o driver de banco usado
    # - Como a query é montada
    conexao = self.__conectar_db()


    conexao.execute(
    "INSERT INTO usuarios ...",
    (self.nome, self.email))

    conexao.fechar()
    
    
# Interface simples e limpa:
usuario = Usuario("Ana", "ana@app.com")
usuario.salvar_no_banco() #