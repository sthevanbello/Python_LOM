"""
Combinations - Ordem não importa
Permutation - Ordem importa

Ambos não repetem valores únicos
Product - Ordem importa e repete valores únicos

"""

from itertools import combinations, permutations, product

pessoas = ['Uguinho', 'Zezinho', 'Luizinho', 'Tio Patinhas', 'Donald', 'Mickey', 'Minie', 'Margarida']

# for grupo in combinations(pessoas, 2):
#     print(grupo)
# for grupo in permutations(pessoas, 2):
#     print(grupo)
for grupo in product(pessoas, repeat=2):
    print(grupo)
