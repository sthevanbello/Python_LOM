import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica_lista(lista):
    resultado = 1
    for item in lista:
        resultado *= item
    return resultado


lista = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(PI)
    print(dobra_lista(lista))
    print(multiplica_lista(lista))
    print(__name__)
