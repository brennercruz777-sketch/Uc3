class CarteiraDigital:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo_inicial = saldo_inicial

    def transferir_pix(self, valor, carteira_destino):
        if self.saldo_inicial >= valor:
            self.saldo_inicial -= valor
            carteira_destino.saldo_inicial += valor
            print(f"Transferência de R$ {valor} realizada com sucesso!")
            print(f"Saldo de {self.nome_titular}: R$ {self.saldo_inicial:.2f}")
            print(f"Saldo de {carteira_destino.nome_titular}: R$ {carteira_destino.saldo_inicial:.2f}")
        else:
            print("Erro: Saldo insuficiente para realizar o PIX.")

cliente_a = CarteiraDigital("Brenner", 500.00)
cliente_b = CarteiraDigital("Rennerb", 100.00)

cliente_a.transferir_pix(150.00, cliente_b)