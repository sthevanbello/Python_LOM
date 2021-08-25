import time

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

# for v in g:
#     print(v)

lista = [x for x in range(1000)]
print(lista)

lista = (x for x in range(1000))
print(lista)

# for v in lista:
#     print(v)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
