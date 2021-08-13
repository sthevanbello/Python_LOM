# entrada = input('Digite a ordem - Crescente ou Decrescente: ')
# ordem = 0
# inicio = 0
# fim = 0
# if entrada.lower() == 'decrescente':
#     ordem = -1
#     inicio = 10
#     fim = -1
# else:
#     ordem = 1
#     inicio = 0
#     fim = 11
# for numero in range(inicio, fim, ordem):
#     print(numero)

lista = list(range(10, 0, -1))

for indice, valor in enumerate(lista):
    print(indice, valor)

print('='*20)

for indice, valor in enumerate(range(10, 1, -1)):
    print(indice, valor)
