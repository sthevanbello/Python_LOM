

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)


def func2(*args, **kwargs):
    print(*args, sep=' - ')
    # kwargs é um dicionário genérico criado se houver um
    # parâmetro nomeado fornecido na chamada da função
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    # Usa-se Get quando não há certeza se a chave existe no dicionário
    nome = kwargs.get('nome')
    print(nome)


lista = [1, 2, 3, 4, 5, 6]
var = func('a', 'b', 'c', 'd', 'e', 'Sthevan', 'f')
var = func2(*lista, nome='Sthevan', sobrenome='Bello')
