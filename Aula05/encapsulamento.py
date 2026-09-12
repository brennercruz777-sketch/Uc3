class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # privado!

    def depositar(self, valor): #Método SETTER
        if valor > 0:
            self.__saldo += valor

    def get_saldo(self): # Método GETTER
        return self.__saldo

minha_conta = ContaBancaria(100)

print(minha_conta.get_saldo())