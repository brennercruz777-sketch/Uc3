class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def alterar_senha(self, senha_antiga, nova_senha):
        if senha_antiga == self.senha:
            senha_antiga = nova_senha
            print("Senha alterada com sucesso.")

        else:
            print("Acesso negado: Senha atual incorreta.")


usuario = Usuario("brenner123", "1234")

usuario.alterar_senha("1234", "abcde")