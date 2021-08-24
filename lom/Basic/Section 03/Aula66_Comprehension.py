lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_exemplo1 = [variavel for variavel in lista1]

print(lista1)
print(lista_exemplo1)

lista_exemplo2 = [v * 2 for v in lista1]
print(lista_exemplo2)

# Para cada valor do primeiro for, cria um segundo valor com o segundo for
exemplo3 = [(v, v2) for v in lista1 for v2 in range(3)]

print(exemplo3)

lista2 = ['Sthevan', 'Bello', 'Alves']

exemplo4 = [v.replace('e', '3') for v in lista2]

print(exemplo4)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
)

exemplo5 = [(x, y) for x, y in tupla]

exemplo5_1 = [(y, x) for x, y in tupla]

exemplo5_dict = dict(exemplo5_1)

print(exemplo5)
print(exemplo5_1)
print(exemplo5_dict)
print(exemplo5_dict['valor2'])

lista3_base = list(range(100))
print(lista3_base)

lista3 = [v for v in lista3_base if v % 2 == 0]
print(lista3)

print('-'*50)

lista3 = [v for v in lista3_base if v % 3 == 0 if v % 8 == 0]
print(lista3)

exemplo7 = [v if v % 3 == 0 else 'N' for v in lista3_base]
print(exemplo7)

exemplo7_2 = [v if v % 3 == 0 and v % 8 == 0 else 'N' for v in lista3_base]
print(exemplo7_2)
