from abstratas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        self.limite = limite
        super().__init__(agencia, conta, saldo)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor=100):
        if valor < 0:
            raise ValueError('Limite não pode ser negativo')
        self.__limite = valor

    def sacar(self, valor):
        if not valor > 0:
            print('Valor não pode ser negativo ou zero')
            return
            # raise ValueError('Valor não pode ser negativo ou zero')
        if not valor <= (self.saldo + self.limite):
            print('Saldo insuficiente')
            return
            # raise ValueError('Saldo insuficiente')
        self.saldo -= valor
