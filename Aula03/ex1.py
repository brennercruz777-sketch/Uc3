class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistido = False

    def marcar_como_assistido(self):

        self.assistido = True
        print(f'O filme {self.titulo} foi assistido!')


filme1 = Filme("Homem Aranha", 120)
filme2 = Filme("Vingadores", 150)

filme1.marcar_como_assistido()
filme2.marcar_como_assistido()