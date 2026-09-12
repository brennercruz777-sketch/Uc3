class AssinaturaBase:
    def __init__(self, usuario):
        self.usuario = usuario

    def calcular_preco(self):
        return 0.0

class AssinaturaPremium(AssinaturaBase):
    def calcular_preco(self):
        super().__init__(usuario)
        return 49.90

class AssinaturaEstudante(AssinaturaBase):
    def calcular_preco(self):
        super().__init__(usuario)
        return 24.90

plano1 = AssinaturaPremium("João")
plano2 = AssinaturaEstudante("Maria")

print(plano1.calcular_preco())
print(plano2.calcular_preco())