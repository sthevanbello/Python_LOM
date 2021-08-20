perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '3',
        },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3 * 3?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '8',
            'd': '9',
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 4 / 4?',
        'respostas': {
            'a': '5',
            'b': '5',
            'c': '1',
            'd': '10',
        },
        'resposta_certa': 'c',
    },
}
acertos = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f'Pergunta: {pergunta_key}: {pergunta_value["pergunta"]} ')

    print('Escolha as opções abaixo:')

    for resposta_key, resposta_value in pergunta_value["respostas"].items():
        print(f'({resposta_key}): {resposta_value}')

    resposta = input("Sua resposta: ")

    if resposta in pergunta_value['resposta_certa']:
        print('Acerto, miserávi')
        acertos += 1
    else:
        print('Burrão...')
    print('-' * 20)
print(f'\nTotal de acertos: {acertos}\n')
