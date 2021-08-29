import re


def calcula_digito(cnpj):
    lista = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj_inteiros = list(map(int, cnpj))
    for numero in range(2):
        lista_multiplica = zip(lista, cnpj_inteiros)
        soma = 0
        for item in lista_multiplica:
            # print(item)
            soma += item[0] * item[1]
            # print(soma)
        cnpj_inteiros.append(aplica_formula(soma))
        lista.insert(0, 6)
    return cnpj_inteiros


def aplica_formula(numero):
    digito = (11 - (numero % 11))
    if digito > 9:
        return 0
    return digito


def valida_cnpj(cnpj):
    cnpj_limpo = remover_caracteres(cnpj)
    cnpj_calculado = ''.join(map(str, calcula_digito(cnpj_limpo[:-2])))

    if cnpj_calculado == cnpj_limpo:
        print(f'O CNPJ: {cnpj} é válido')
    else:
        print(f'O CNPJ: {cnpj} é inválido')


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


cnpj1 = '04252011000110'
cnpj2 = '14038460000113'
cnpj3 = '46637543000115'
cnpj4 = '19302902000100'
cnpj5 = '43833353000185'
cnpj6 = '04.252.011/0001-10'

valida_cnpj(cnpj1)
valida_cnpj(cnpj2)
valida_cnpj(cnpj3)
valida_cnpj(cnpj4)
valida_cnpj(cnpj5)
valida_cnpj(cnpj6)
