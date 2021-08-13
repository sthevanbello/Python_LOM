from random import randint


def cria_cpf(numero):
    multiplicacao = 0
    for i in range(2):
        soma = 0
        for indice, multiplicador in enumerate(range(10+i, 1, -1)):

            multiplicacao = int(numero[indice]) * multiplicador

            soma += multiplicacao
            print(f'{numero[indice]} * {multiplicador} = {multiplicacao}')

        numero += confere_ultimos_digitos(soma)
    return numero


def confere_ultimos_digitos(soma):
    digito = 11 - (soma % 11)
    digito_verificado = 0 if (digito > 9) else digito
    return str(digito_verificado)


numero = str(randint(100000000, 999999999))
novo_cpf = cria_cpf(numero)

print(novo_cpf)
