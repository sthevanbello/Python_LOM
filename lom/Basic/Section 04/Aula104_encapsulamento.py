"""
public, protected, private
_ = private / protected (public com 1 underline)
__ = private (_NOMEDACLASSE__nome_atributo)

"""


class BaseDe_dados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'id: {id} - Nome: {nome}')

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDe_dados()

bd.inserir_cliente(1, 'Homer')
bd.inserir_cliente(2, 'Marge')
bd.inserir_cliente(3, 'Bart')

print('=' * 50)
print(bd.dados)
bd.lista_clientes()
bd.apaga_cliente(2)
print('=' * 50)
bd.lista_clientes()
