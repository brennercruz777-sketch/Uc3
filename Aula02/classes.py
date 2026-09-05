class Cachorro:
    #Método Constructor
    def __init__(self,nome, raca, tamanho, cor_pelo): #Atributos da classe
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo
        self.patas = 4


zeca = Cachorro("Zeca", "Viralata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marron")





class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = True

    #Método de uma classe
    def desativar_conta(self):
        self.ativo = False

    def mudar_nome(self):
        self.nome = input('Digite seu novo nome de usuário')

nova_conta = Usuario("Brenner", "brenner@gmail.com")

nova_conta.desativar_conta()

print(nova_conta.ativo)