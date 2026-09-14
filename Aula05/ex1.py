class Usuario:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    # Método GETTER - NÃO FAZ PARTE DO EXERCÍCIO
    def get_login(self):
        return self.__login

    # Método SETTER
    def alterar_senha(self, senha_antiga):
        if senha_antiga == self.__senha:
            #So pergunda a senha nova se acertar a atual
            self.__senha = input('Digite sua nova senha:\n-->')
            print("Senha alterada com sucesso.")
        else:
            print("Acesso negado: Senha atual incorreta.")

usuario = Usuario("brenner123", "1234")

usuario.alterar_senha(input('Digite sua seha atual:\n-->'))