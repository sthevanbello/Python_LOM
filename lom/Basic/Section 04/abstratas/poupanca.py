from abstratas.conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
