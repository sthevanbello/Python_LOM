from dados import lista, produtos, pessoas


def aumenta_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.1, 2)
    return produto


def aumenta_idade(p):
    p['idade'] = p['idade'] * 1.2
    return p
# print(lista)
# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)

# novos_produtos = map(lambda p: p['preco'], produtos)
# for produto in novos_produtos:
#     print(produto)

# novos_produtos2 = map(aumenta_preco, produtos)

# for produto in novos_produtos2:
#     print(produto)

# nome_pessoas = map(lambda n: n['nome'], pessoas)
nome_pessoas = map(aumenta_idade, pessoas)

for pessoa in nome_pessoas:
    print(pessoa)
