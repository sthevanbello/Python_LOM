def confere_cpf(cpf):
    multiplicacao = 0
    digito = ''
    for i in range(2):
        soma = 0
        for indice, multiplicador in enumerate(range(10+i, 1, -1)):

            multiplicacao = int(cpf[indice]) * multiplicador

            soma += multiplicacao
            print(f'{cpf[indice]} * {multiplicador} = {multiplicacao}')

        digito += confere_ultimos_digitos(soma)

    return digito


def confere_ultimos_digitos(soma):
    digito = 11 - (soma % 11)
    digito_verificado = 0 if (digito > 9) else digito
    return str(digito_verificado)


# cpf = '22987301804'
cpf = input('Digite um CPF apenas com números: ')
novo_cpf = cpf[:9] + confere_cpf(cpf)

print(novo_cpf)

if cpf == novo_cpf:
    print('CPF válido')
else:
    print('cpf inválido')
