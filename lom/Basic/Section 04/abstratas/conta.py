from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('Valor não é numérico')
        if valor < 0:
            raise ValueError('Valor não pode ser negativo')
        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('Valor não é numérico')
        if valor < 0:
            raise ValueError('Valor não pode ser negativo')
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass
