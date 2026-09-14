class Animal:
    def __init__(self, membros, orgaos):
        self.membros = membros
        self.orgaos = orgaos
    
    def comer(self):
        print("hmmm")

    def reproduzir(self, parceiro):
        return self + parceiro
    
class Ave(Animal):
    def __init__(self, membros, orgaos, pena):
        super().__init__(membros, orgaos)
        self.penas = pena

    def voar(self):
        print("*Asa batendo")

class Mamifero(Animal):
    def __init__(self, membros, orgaos, pelo):
        super().__init__(membros, orgaos)
        self.pelo = pelo

    def beber_leite(self):
        print("hmmm leite")

class Primata(Mamifero):
    def __init__(self, membros, orgaos, pelo):
        super().__init__(membros, orgaos, pelo)
        self.polegares = 2

class Morcego(Mamifero):
    def __init__(self, membros, orgaos, pelo):
        # Morcegos têm pelos, então passamos para o construtor de Mamifero
        super().__init__(membros, orgaos, pelo)

    def voar(self):
        # Aqui está o polimorfismo: ele se comporta como uma Ave!
        print("*Asa (de pele) batendo: Flap Flap!*")
    
    def sonar(self):
        print("Beeeep! Tem uma parede ali!")

bentevi = Ave(membros=4, orgaos="todos", pena="branca e amarela")
batman = Morcego(membros=4, orgaos="todos", pelo="preto")

print(f"O morcego tem pelo {batman.pelo}:")
batman.beber_leite() # Comportamento de Mamífero
batman.voar()        # Comportamento "emprestado" da lógica de Ave
bentevi.voar()



#-----------------------------------------------------
class SMS(Notificacao):
    def __init__(self, destinatario, texto, numero):
        super().__init__(destinatario, texto)
        self.numero = numero
    def enviar(self):
        print(f"SMS enviado para {self.numero}: {self.texto}")

class Push(Notificacao):
    def __init__(self, destinatario, texto, device_token):
        super().__init__(destinatario, texto)
        self.device_token = device_token
    def enviar(self):
        print(f"Push via FCM para {self.device_token}: {self.texto}")

    def processar_fila(notificacoes):
        for n in notificacoes:
        n.enviar()
        
# Exemplo de uso
fila = [
 Email("user@ex.com", "Olá!"),
 SMS("user", "Oi", "99999999"),
 Push("user", "Alerta", "token123")
]
processar_fila(fila)
