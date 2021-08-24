lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
    ('chave4', 'valor4'),
]

dicionario = dict(lista)
print(lista)
print(dicionario)

d1 = {x: y for x, y in lista}
print(d1)

d1 = {f'Chave_{x}': f'Valor_{x**2}' for x in range(5)}

print(d1)
