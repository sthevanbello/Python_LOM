import re
import random


def valida_cnpj(cnpj):
    cnpj_limpo = remover_caracteres(cnpj)
    cnpj_calculado = ''.join(map(str, calcula_digito(cnpj_limpo)))

    if cnpj_calculado == cnpj_limpo:
        print(f'O CNPJ: {cnpj} é válido')
    else:
        print(f'O CNPJ: {cnpj} é inválido')


def verifica_sequencia(cnpj):
    cnpj = str(cnpj)
    sequencia = cnpj[0] * len(cnpj)
    if cnpj == sequencia:
        return False
    return True


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def calcula_digito(cnpj):
    cnpj = cnpj[:-2]
    if verifica_sequencia(cnpj):
        lista = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        cnpj_inteiros = list(map(int, cnpj))
        for numero in range(2):
            lista_multiplica = zip(lista, cnpj_inteiros)
            soma = 0
            for item in lista_multiplica:
                soma += item[0] * item[1]
            cnpj_inteiros.append(aplica_formula(soma))
            lista.insert(0, 6)
        return cnpj_inteiros
    else:
        return cnpj


def aplica_formula(numero):
    digito = (11 - (numero % 11))
    if digito > 9:
        return 0
    return digito


def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = ''.join(map(str, calcula_digito(inicio_cnpj)))
    return novo_cnpj



cnpj1 = '04252011000110'
cnpj2 = '14038460000113'
cnpj3 = '46637543000115'
cnpj4 = '19302902000100'
cnpj5 = '43833353000185'
cnpj6 = '04.252.011/0001-10'
cnpj7 = '11.111.111/1111-11'
cnpj8 = '00.000.000/0000-00'
cnpj9 = '123456'
cnpj10 = '123rgregreer456'

# valida_cnpj(cnpj1)
# valida_cnpj(cnpj2)
# valida_cnpj(cnpj3)
# valida_cnpj(cnpj4)
# valida_cnpj(cnpj5)
# valida_cnpj(cnpj6)
# valida_cnpj(cnpj7)
# valida_cnpj(cnpj8)
# valida_cnpj(cnpj9)
# valida_cnpj(cnpj10)
cnpj = gera()
valida_cnpj(cnpj)
