def divide(n1, n2):
    # try:
    #     return n1/n2
    # except ZeroDivisionError as error:
    #     print(error)
    #     raise
    if n2 == 0:
        raise ValueError('O segundo número não pode ser zero')
    return n1 / n2


# try:
#     print(divide(2, 0))
# except Exception as error:
#     print(error)

try:
    print(divide(2, 0))
except ValueError as error:
    print(error)


def converte_numero(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Erro: Não é um valor válido')
    else:
        print(numero * 5)
