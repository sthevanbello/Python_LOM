# cpf = input('Digite o cpf - Apenas números: ')

# cpf = '22987301804'

def confere_penultimo(cpf):
    multiplicacao = 0
    soma = 0
    
    for indice, multiplicador in enumerate(range(10, len(cpf)-10, -1)):

        multiplicacao = int(cpf[indice]) * multiplicador

        soma += multiplicacao

        print(f'{cpf[indice]} * {multiplicador} = {multiplicacao}')

    return soma


def confere_ultimo(cpf):
    multiplicacao = 0
    soma = 0
    for indice, multiplicador in enumerate(range(11, len(cpf)-10, -1)):

        multiplicacao = int(cpf[indice]) * multiplicador

        soma += multiplicacao

        print(f'{cpf[indice]} * {multiplicador} = {multiplicacao}')

    return soma


def confere_ultimos_digitos(soma):
    digito = 11 - (soma % 11)
    digito_verificado = 0 if (digito > 9) else digito
    return str(digito_verificado)


cpf = '22987301804'
novo_cpf = cpf[:9]

soma = confere_penultimo(cpf)
novo_cpf += confere_ultimos_digitos(soma)
soma = confere_ultimo(cpf)
novo_cpf += confere_ultimos_digitos(soma)

print(novo_cpf)

if cpf == novo_cpf:
    print('CPF válido')
else:
    print('cpf inválido')
