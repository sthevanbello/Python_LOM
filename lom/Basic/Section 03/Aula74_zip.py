from itertools import zip_longest, count


indice = count()
cidades = ['São Paulo', 'Curitiba', 'Belo Horizonte', 'Florianópolis', 'Porto Alegre', 'Rio Branco', 'Salvador ']
estados = ['SP', 'PR', 'MG', 'SC', 'RS']
# cidades_estados = zip(estados, cidades)
# zip_longest une pela lista maior colocando none onde não houver dado
# cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')
cidades_estados = zip(indice, estados, cidades)
print(type(cidades_estados))
# print(next(cidades_estados))

# print(dict(cidades_estados))

# print(list(cidades_estados))
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
