from typing import Type


class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade
        self.__enderecos = []

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

    def insere_endereco(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

