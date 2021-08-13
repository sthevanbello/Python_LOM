"""
Split, Join, Enumerate
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos de objetos iteráveis
"""
frase1 = "O Brasil é o país do futebol. O Brasil é Penta"
frase2 = "Salve o Corinthians, o Campeão dos Campeões"
primeira_lista = frase1.split(' ')
segunda_lista = frase2.split(' ')
print(primeira_lista)
print(segunda_lista)

# for valor in primeira_lista:
#     print(f'{valor} - {primeira_lista.count(valor)}')

lista = ','.join(frase2)
print(lista)

for index, valor in enumerate(frase2):
    print(f'{index} - {valor}')

nova_lista = [
    [0, 'Sthevan'],
    [1, 'Natália'],
    [2, 'Bolão'],
    [3, 'Pretinha']
]

for indice, nome in nova_lista:
    print(f'{indice} - {nome}')
