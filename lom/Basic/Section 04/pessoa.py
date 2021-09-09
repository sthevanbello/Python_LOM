from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def get_ano_nascimento(self, ano_atual):
        return ano_atual - self.__idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Métodos estáticos não recebem nem a classe (cls) e nem instância (self)
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
