from typing import Type


class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise TypeError(
                'Formato da idade precisa de ser em número inteiro')
        else:
            self.__idade = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        self.cpf = cpf
        super().__init__(nome, idade)

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if not len(valor) == 11:
            raise ValueError('CPF incompleto')
        else:
            self.__cpf = valor

    def comprar(self):
        print("Cliente normal comprando")


class ClienteVip(Cliente):
    def __init__(self, nome, idade, cpf, cartao_vip):
        self.cartao_vip = cartao_vip
        super().__init__(nome, idade, cpf)

    @property
    def cartao_vip(self):
        return self.__cartao_vip

    @cartao_vip.setter
    def cartao_vip(self, valor):
        self.__cartao_vip = valor

    def comprar(self):
        print('-' * 50)
        super().comprar()
        print(f'Executando o método comprar de dentro do ClienteVip.')
        print("Cliente VIP comprando")


class ClienteEspecial(ClienteVip, Cliente):
    def __init__(self, nome, idade, cpf, cartao_vip, cartao_especial):
        super().__init__(nome, idade, cpf, cartao_vip)
        self.cartao_especial = cartao_especial

    @property
    def cartao_especial(self):
        return self.__cartao_especial

    @cartao_especial.setter
    def cartao_especial(self, valor):
        self.__cartao_especial = valor
