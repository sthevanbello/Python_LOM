lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_zip = zip(lista_a, lista_b)

lista_soma = [x + y for x, y in lista_zip]

print(lista_soma)
