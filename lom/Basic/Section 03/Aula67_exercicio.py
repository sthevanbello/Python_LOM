numeros = '012345678901234567890123456789012345678901234567890123456789'

lista = []
parte = ''
n = 10
for valor in numeros:
    parte += valor
    if valor == '9':
        lista.append(parte)
        parte = ''

print(lista)

comp = [numeros[i:i+n] for i in range(0, len(numeros), n)]

print(f'comp: {comp}')

retorno = '.'.join(lista)

print(retorno)
