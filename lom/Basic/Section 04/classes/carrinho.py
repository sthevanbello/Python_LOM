from functools import reduce


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def lista_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):

        soma = reduce(lambda a, v: v + a, self.__produtos, 0)
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        # return total
        return soma


class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor
