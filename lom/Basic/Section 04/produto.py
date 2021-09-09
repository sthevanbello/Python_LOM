class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    # Getter
    @property
    def preco(self):
        return self.__preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self.__preco = valor

    def desconto(self, percentual):
        return self.__preco - (self.__preco * percentual / 100)
