from abstratas.conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if not valor > 0:
            print('Valor não pode ser negativo ou zero')
            return
            # raise ValueError('Valor não pode ser negativo ou zero')
        if not valor <= self.saldo:
            print('Saldo insuficiente')
            return
            # raise ValueError('Saldo insuficiente')
        self.saldo -= valor
