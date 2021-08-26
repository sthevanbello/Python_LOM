from dados import lista, produtos, pessoas


def filtra(produto):
    if produto['preco'] > 50:
        produto['status'] = 'eh caro'
    return True


def filtra_idade(pessoa):
    if pessoa['idade'] > 13:
        return True


nova_lista = filter(lambda n: n > 5, lista)

for numero in nova_lista:
    print(numero)

produtos_filtrados = filter(lambda p: p['preco'] > 20, produtos)

for produto in produtos_filtrados:
    print(produto)

produtos_filtrados2 = filter(filtra, produtos)

print('=' * 100)
for produto in produtos_filtrados2:
    print(produto)

pessoa_filtrada = filter(filtra_idade, pessoas)

print('=' * 100)
for pessoa in pessoa_filtrada:
    print(pessoa)
