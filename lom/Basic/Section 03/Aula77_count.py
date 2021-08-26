from itertools import count

# count é um iterador que não tem fim

contador1 = count()
# contador2 = count(start=5, step=2)
# contador2 = count(start=5, step=0.01)
contador2 = count(start=9, step=-0.1)
contador3 = count()

print(next(contador1))
print(next(contador1))

for valor in contador2:
    # print(f'{valor:.2f}')
    # if valor >= 10:
    if valor >= 10 or valor < -10:
        break
    print(f'{round(valor, 2)}')

lista = ['Luizinho', 'Uguinho', 'Zezinho', 'Tio Patinhas', 'Asnésio', 'Donald']
lista = zip(contador3, lista)
print(list(lista))
