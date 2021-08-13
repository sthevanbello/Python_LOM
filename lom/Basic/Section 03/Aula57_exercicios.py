
def funcao1(funcao):
    return funcao()


def funcao2():
    return 'Função 2'


def funcao_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao3(nome):
    return f'Nome: {nome}'


def funcao4(mensagem, nome):
    return f'{mensagem}, {nome}'


variavel = funcao1(funcao2)
print(variavel)

executa_mestre = funcao_mestre(funcao3, 'Sthevan')
print(executa_mestre)

executa_mestre2 = funcao_mestre(funcao4, 'Olá', 'Sthevan')
print(executa_mestre2)
