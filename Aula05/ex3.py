class AssinaturaBase:
    def __init__(self,usuario):
        self.usuario = usuario

    def calcular_preco(self):
        return 0.00

class AssinaturaPremium(AssinaturaBase):
    def __init__(self, usuario):
        super().__init__(usuario)

    def calcular_preco(self):
        return 49.90

class AssinaturaEstudante(AssinaturaBase):
    def __init__(self, usuario):
        super().__init__(usuario)

    def calcular_preco(self):
        return 24.90


assinaturas = [AssinaturaBase("1"), AssinaturaPremium("2"), AssinaturaEstudante("3")]


for i in assinaturas:
    print("valor da assinatura R$", i.calcular_preco())