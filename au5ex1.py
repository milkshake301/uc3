class Usuario:
    def __init__(self, login, senha):
        self.login = login    
        self.__senha = senha 

    def alterar_senha(self, senha_antiga, nova_senha):
        if senha_antiga == self.__senha:
            self.__senha = nova_senha
            print("Senha alterada com sucesso")
        else:
            print("Acesso negado: Senha atual incorreta")


print("--- Teste Exercício 1: Encapsulamento ---")
usuario = Usuario("admin", "12345")


usuario.alterar_senha(input(""), input("")) 


usuario.alterar_senha(input(""), input("")) 
print()