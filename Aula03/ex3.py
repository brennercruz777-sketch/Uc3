class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Novo valor: {self.saldo}')


    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Valor sacado: R$ {valor}")
        else:
            print("Saque negado: Saldo insuficiente.")

conta1 = ContaBancaria('Brenner')

conta1.depositar(100)
conta1.sacar(150)
conta1.sacar(50)

