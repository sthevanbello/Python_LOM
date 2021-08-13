lista = [
    ['Sabonete', 13],
    ['Tomate', 6],
    ['Papel Higiênico', 5],
    ['Ovo', 24],
    ['Banana', 17]
]


def funcao(item):
    return item[1]


# a = lambda x, y: x * y
# print(a(5, 6))
# lista.sort(key=funcao)

# lista.sort(key=lambda item: item[1])

print(lista)
print(sorted(lista))
print(sorted(lista, key=lambda p: p[1]))
print(sorted(lista, key=lambda p: p[1], reverse=True))
print(lista)
print(sorted(lista, key=lambda n: n[0]))
